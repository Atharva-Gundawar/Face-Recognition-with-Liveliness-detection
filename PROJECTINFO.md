
# Attendance With Liveliness Detection

## File Structure

```markdown
  ├── .gitignore                                      <- Gitignore file
  ├── attendance.csv                                  <- Recorded attendance database
  ├── face_detector                                   <- Face detector models
  │   ├── deploy.prototxt                             
  │   └── res10_300x300_ssd_iter_140000.caffemodel    
  ├── known_faces                                     <- Faces which should be recognized by the face recognizer
  ├── le.pickle                                       <- Supporting pickle file for face detection
  ├── LICENSE                                         
  ├── livelinessModel                                 
  │   └── livenessnet.py                              <- Livliness detection model class
  ├── liveness.model                                  <- Livliness model
  ├── plot.png                                        <- Accuracy Plot 
  ├── PROJECTINFO.md                                  
  ├── README.md                                       
  ├── requirements.txt                                <- Install using pip install -r requirements.txt
  ├── src                                             
  │   ├── FaceRecogOnFeed.py                          <- Face recognition implimentation on live feed
  │   ├── FaceRecogOnImage.py                         <- Face recognition implimentation on image
  │   ├── gather_examples.py                          <- Genrates dataset for training the liveness model
  │   ├── jsExample.py                                <- Face recognition with JavaScript support
  │   ├── LivelinessOnFeed.py                         <- Liveliness video implimentation
  │   ├── livenessDemo.py                             <- Liveliness image implimentation
  │   └── trainModel.py                               <- To train the Liveliness model
  └── videos                                          <- Videos for making the dataset

```

## Contributing

1. Fork it (<https://github.com/Atharva-Gundawar/Face-Recognition-with-Liveliness-detection>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
