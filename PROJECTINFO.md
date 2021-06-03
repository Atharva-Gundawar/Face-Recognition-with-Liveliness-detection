# Attendance With Liveliness Detection

## File Structure

```markdown
  ├── .gitignore                                      <- DSC
  ├── .vscode                                         <- DSC
  │   └── settings.json                               <- DSC
  ├── attendance.csv                                  <- DSC
  ├── facerecogizer2.py                               <- DSC
  ├── face_detector                                   <- DSC
  │   ├── deploy.prototxt                             <- DSC
  │   └── res10_300x300_ssd_iter_140000.caffemodel    <- DSC
  ├── frwithvideo.py                                  <- DSC
  ├── gather_examples.py                              <- DSC
  ├── known_faces                                     <- DSC
  │   ├── Ashikka                                     <- DSC
  │   │   ├── 100.png                                 <- DSC
  │   │   ├── 101.png                                 <- DSC
  │   │   ├── 102.png                                 <- DSC
  │   │   ├── 103.png                                 <- DSC
  │   │   ├── 104.png                                 <- DSC
  │   │   ├── 105.png                                 <- DSC
  │   │   ├── 106.png                                 <- DSC
  │   │   ├── 107.png                                 <- DSC
  │   │   ├── 125.png                                 <- DSC
  │   │   ├── 126.png                                 <- DSC
  │   │   ├── 127.png                                 <- DSC
  │   │   ├── 128.png                                 <- DSC
  │   │   ├── 129.png                                 <- DSC
  │   │   ├── 130.png                                 <- DSC
  │   │   ├── 131.png                                 <- DSC
  │   │   ├── 132.png                                 <- DSC
  │   │   ├── 133.png                                 <- DSC
  │   │   ├── 134.png                                 <- DSC
  │   │   ├── 43.png                                  <- DSC
  │   │   ├── 44.png                                  <- DSC
  │   │   ├── 45.png                                  <- DSC
  │   │   ├── 46.png                                  <- DSC
  │   │   ├── 47.png                                  <- DSC
  │   │   ├── 48.png                                  <- DSC
  │   │   ├── 49.png                                  <- DSC
  │   │   ├── 50.png                                  <- DSC
  │   │   ├── 51.png                                  <- DSC
  │   │   ├── 52.png                                  <- DSC
  │   │   ├── 70.png                                  <- DSC
  │   │   ├── 71.png                                  <- DSC
  │   │   ├── 72.png                                  <- DSC
  │   │   ├── 73.png                                  <- DSC
  │   │   ├── 74.png                                  <- DSC
  │   │   ├── 75.png                                  <- DSC
  │   │   ├── 76.png                                  <- DSC
  │   │   ├── 77.png                                  <- DSC
  │   │   ├── 78.png                                  <- DSC
  │   │   ├── 79.png                                  <- DSC
  │   │   ├── 98.png                                  <- DSC
  │   │   └── 99.png                                  <- DSC
  │   └── David                                       <- DSC
  │       ├── 0.png                                   <- DSC
  │       ├── 1.png                                   <- DSC
  │       ├── 10.png                                  <- DSC
  │       ├── 11.png                                  <- DSC
  │       ├── 12.png                                  <- DSC
  │       ├── 13.png                                  <- DSC
  │       ├── 14.png                                  <- DSC
  │       ├── 15.png                                  <- DSC
  │       ├── 16.png                                  <- DSC
  │       ├── 17.png                                  <- DSC
  │       ├── 18.png                                  <- DSC
  │       ├── 19.png                                  <- DSC
  │       ├── 2.png                                   <- DSC
  │       ├── 20.png                                  <- DSC
  │       ├── 21.png                                  <- DSC
  │       ├── 22.png                                  <- DSC
  │       ├── 23.png                                  <- DSC
  │       ├── 24.png                                  <- DSC
  │       ├── 25.png                                  <- DSC
  │       ├── 26.png                                  <- DSC
  │       ├── 27.png                                  <- DSC
  │       ├── 28.png                                  <- DSC
  │       ├── 29.png                                  <- DSC
  │       ├── 3.png                                   <- DSC
  │       ├── 30.png                                  <- DSC
  │       ├── 31.png                                  <- DSC
  │       ├── 32.png                                  <- DSC
  │       ├── 33.png                                  <- DSC
  │       ├── 34.png                                  <- DSC
  │       ├── 35.png                                  <- DSC
  │       ├── 36.png                                  <- DSC
  │       ├── 37.png                                  <- DSC
  │       ├── 38.png                                  <- DSC
  │       ├── 39.png                                  <- DSC
  │       ├── 4.png                                   <- DSC
  │       ├── 40.png                                  <- DSC
  │       ├── 41.png                                  <- DSC
  │       ├── 42.png                                  <- DSC
  │       ├── 43.png                                  <- DSC
  │       ├── 44.png                                  <- DSC
  │       ├── 5.png                                   <- DSC
  │       ├── 6.png                                   <- DSC
  │       ├── 7.png                                   <- DSC
  │       ├── 8.png                                   <- DSC
  │       └── 9.png                                   <- DSC
  ├── le.pickle                                       <- DSC
  ├── LICENSE                                         <- DSC
  ├── livelinessModel                                 <- DSC
  │   └── livenessnet.py                              <- DSC
  ├── liveness.model                                  <- DSC
  ├── livenesss.model                                 <- DSC
  ├── liveness_demo.py                                <- DSC
  ├── plot.png                                        <- DSC
  ├── README.md                                       <- DSC
  ├── requirements.txt                                <- DSC
  ├── src                                             <- DSC
  │   └── run.py                                      <- DSC
  └── train.py                                        <- DSC

```

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
