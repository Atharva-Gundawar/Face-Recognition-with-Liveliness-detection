import face_recognition
import os
import cv2
from imutils.video import VideoStream
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import time
from datetime import datetime 

def markAttendance(name):
  with open('./attendance.csv', 'r+') as f:
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

KNOWN_FACES_DIR = 'known_faces'
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'hog'  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model


print('Loading known faces...')
known_faces = []
known_names = []
def name_to_color(name):
    # Take 3 first letters, tolower()
    # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
    color = [(ord(c.lower())-97)*8 for c in name[:3]]
    return color

for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
        try:
            image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(encoding)
            known_names.append(name)
        except:
            pass


print('Processing unknown faces...')
# Now let's loop over a folder of faces we want to label

print("[INFO] loading face detector...")
protoPath = os.path.sep.join(["face_detector", "deploy.prototxt"])
modelPath = os.path.sep.join(["face_detector", "res10_300x300_ssd_iter_140000.caffemodel"])
net = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

print("[INFO] loading liveness detector...")
livemodel = load_model("liveness.model")
le = pickle.loads(open("le.pickle", "rb").read())

print("[INFO] starting video stream...")

video =cv2.VideoCapture(0)
frameNum = 0
maxFrames = 5
while True:

    ret,image = video.read()
    crop_img = image
    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)
    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:  # If at least one is true, get a name of first of found labels
            match = known_names[results.index(True)]
            # print(f' - {match} from {results}')

            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            color = name_to_color(match)
            print(face_location)
            cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)
            crop_img = image[face_location[0]:face_location[2], face_location[3]:face_location[1]]
            crop_img = cv2.resize(crop_img, (32, 32))
            crop_img = crop_img.astype("float") / 255.0
            crop_img = img_to_array(crop_img)
            crop_img = np.expand_dims(crop_img, axis=0)

            # pass the face ROI through the trained liveness detector
            # model to determine if the face is "real" or "fake"
            preds = livemodel.predict(crop_img)[0]
            j = np.argmax(preds)
            label = le.classes_[j]
            print(preds[j])

            if frameNum<maxFrames : 
                if label == "real":
                    frameNum+=1
                else:
                    frameNum = 0
            else:
                markAttendance(str(match))
                frameNum = 0


            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2] + 22)
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
            cv2.putText(image, label+match+str(frameNum), (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)
    cv2.imshow("filename", image)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
cv2.destroyAllWindows()