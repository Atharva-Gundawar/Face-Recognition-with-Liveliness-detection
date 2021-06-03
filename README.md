# Attendance With Liveliness Detection

## How to start

### Train your own Liveliness Detection model

- Store real and fake videos in the videos directory, then run

```bash
python src/gather_examples.py --input videos/real.mov --output dataset/real --detector face_detector --skip 1
python src/gather_examples.py --input videos/fake.mp4 --output dataset/fake --detector face_detector --skip 4
```

- Train the model using the following command

```bash
python src/trainModel.py --dataset dataset --model liveness.model --le le.pickle
```

this will create `liveness.model` file

- Add faces to known_faces directory.

- To test run the following command

```bash
python src\FaceRecogOnFeed.py
```

## Abstract

The aim of this project is to automate the process of taking attendance in various educational institutions. With the help of this project, one can get their attendance marked by simply facing a camera. Their details - name, time of arrival, date, and registration number will be automatically stored in a .csv file.

Although many face recognition algorithms have been developed over the years, their speed and accuracy balance has not been quite optimal. But some recent advancements have shown promise. A good example is Facebook, where they are able to tag you and your friends with just a few images of training and with accuracy as high as 98%. Here, I have tried to replicate similar results using a face recognition library developed by Adam Geitgey.
Face recognition has a series of problems:

- First, look at a picture and find all the faces in it

- Second, focus on each face and be able to understand that even if a face is turned in a weird direction or in bad lighting, it is still the same person.

- Third, be able to pick out unique features of the face that you can use to tell it apart from other people— like how big the eyes are, how long the face is, etc.

- Fourth, compare the unique features of that face to all the people you already know to determine the person’s name.

- Finally, to create a liveness detector capable of spotting fake faces and performing anti-face spoofing in face recognition systems.

## Algorithm

There exist various algorithms for Facial Recognition, namely the Kohonen approach, Principal Component Analysis (PCA), Fisherfaces, and the traditional Local Binary Patterns (LBP). Viola-Jones object detection framework was one of the first detection algorithms to provide competitive and accurate detection rates. However, in this project, the HOG or the Histogram of Oriented Gradients algorithm is used for the feature identification, after which, we use the SVM algorithm (Support Vector Machine) as a classifier.

The HOG algorithm was chosen since it is better suited for facial recognition as compared to the other algorithms specified. In most algorithms, for example, Voila-Jones, Haar features are identified followed by training a classifier to identify these features. These features include the location and size of the eyes, mouth, etc. Then a learning algorithm learns the specifics of these facial features and uses them to identify the person.
In the HOG method, patterns in the face are identified instead of specific features. A pixel is identified in each region, and the pixels surrounding it are observed. A vector is drawn from this pixel to the direction of the darker pixels. Thus, gradually, all pixels are replaced by a map of arrows, which is unique for every person.

The Voila-Jones algorithm gives an accuracy of about 90% only if each classifier has been trained to get an accuracy of about 99.7%, and it gives a false positive rate of about 65%. On the other hand, HOG naturally gives an accuracy of about 98%, which is almost as good as humans do for recognizing faces. A modified version of this algorithm is also used by Facebook in identifying people in pictures! It is not only faster, but also more efficient.
The following diagram demonstrates a comparative analysis of HOG with SVM classifiers against other popular facial recognition algorithms. For all datasets, except Georgia Tech, HOG gives a higher facial recognition rate, which makes it suitable to use in this project.

## Liveliness Detection

Facial recognition systems are easily fooled by “spoofing” and “non-real” faces.
Face recognition systems can be circumvented simply by holding up a photo of a person (whether printed, on a smartphone, etc.) to the face recognition camera.
In order to make face recognition systems more secure, we need to be able to detect such fake/non-real faces — liveness detection is the term used to refer to such algorithms.
There are a number of approaches to liveness detection, including:

- Texture analysis, including computing Local Binary Patterns (LBPs) over face regions and using an SVM to classify the faces as real or spoofed.
- Frequency analysis, such as examining the Fourier domain of the face.
- Variable focusing analysis, such as examining the variation of pixel values between two consecutive frames.
- Heuristic-based algorithms, including eye movement, lip movement, and blink detection. These sets of algorithms attempt to track eye movement and blinks to ensure the user is not holding up a photo of another person (since a photo will not blink or move its lips).
- Optical Flow algorithms, namely examining the differences and properties of optical flow generated from 3D objects and 2D planes.
- 3D face shape, similar to what is used on Apple’s iPhone face recognition system, enabling the face recognition system to distinguish between real faces and printouts/photos/images of another person.
- Combinations of the above, enabling a face recognition system engineer to pick and choose the liveness detections models appropriate for their particular application.

For this project, I’ll be treating liveness detection as a binary classification problem.
Given an input image, we’ll train a Convolutional Neural Network capable of distinguishing real faces from fake/spoofed faces and then use the model to separate them. This feature will help us mark attendance for the students that are physically present and won’t let and fake/spoofed faces surpass the system.

## Objectives

- To be able to detect faces using a webcam
- To be able to compare the faces with the faces in the database, and granting attendance to the recognised face
- To be able to make our model spoof-proof, using liveliness detection, so that fake faces cannot surpass the system
- Adding a blinking feature, to cross check if there is a real person facing the camera

## Languages

The code for this project will be written in Python 3.

## Libraries Required

- opencv-python
- face_recognition
- cv2
- numpy
- tensorflow
- matplotlib
- sklearn
- os
- pickle

## Resources

- <https://www.pyimagesearch.com/2019/03/11/liveness-detection-with-opencv>
- <https://www.murtazahassan.com/face-recognition-and-attendance-system>
