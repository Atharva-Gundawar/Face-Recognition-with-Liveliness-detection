import cv2
from matplotlib import pyplot as plt
import numpy as np
import face_recognition
import os
from base64 import b64decode
from datetime import datetime

path = '/content/images'
images = []
classNames = []
k = 0

myList = os.listdir(path)
myList.pop(0)
print(myList)


for image in myList:
  currentImage = cv2.imread(f'{path}/{image}')
  images.append(currentImage)
  classNames.append(os.path.splitext(image)[0])
print(classNames)

def findEncodings(images):
  encodeList = []
  for i in images:
    encode = face_recognition.face_encodings(i)[0]
    encodeList.append(encode)
  return encodeList

def markAttendance(name):
  with open('/content/sample_data/attendance.csv', 'r+') as f:
    myDataList = f.readlines()
    nameList = []
    for line in myDataList:
      entry = line.split(',')
      nameList.append(entry[0])
    if name not in nameList:
        now = datetime.now()
        time = now.strftime('%X')
        date = now.strftime('%x')
        f.writelines(f'\n{name},{date},{time}')

def take_photo(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

try:
  filename = take_photo()
  print('Saved to {}'.format(filename))
  display(Image(filename))
except Exception as err:
  print(str(err))

encodeListKnown = findEncodings(images)
print('Encoding complete')

while True:
  img = cv2.imread('/content/photo.jpg') 
  imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)

  faceCurrentFrame = face_recognition.face_locations(imgS)
  encodesCurrentFrame = face_recognition.face_encodings(imgS, faceCurrentFrame)

  if k != 0:
    k = 0
    break

  else:
    for encodeFace, faceLoc in zip(encodesCurrentFrame, faceCurrentFrame):
      matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
      faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
      matchIndex = np.argmin(faceDis)

      if matches[matchIndex]:
        name = classNames[matchIndex].upper()
        print(name)
        k = k + 1
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
        cv2.rectangle(img,(x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        markAttendance(name)

      else:
          print('Human not found')
          break

  plt.imshow(img) 
  cv2.waitKey(1)
