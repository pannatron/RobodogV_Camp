# Introduction to Advanced Computer Vision with Python - Day 4
Welcome to Day 4 of our Python Programming Course! Today, we will delve into advanced computer vision techniques utilizing two powerful libraries: Mediapipe and CVzone. These tools offer pre-built models and functions that simplify the implementation of complex computer vision tasks such as facial recognition, hand tracking, and object detection.

### Setting Up
To get started with today's exercises, you need to install Mediapipe and CVzone. Follow these installation steps:

Install Mediapipe and CVzone
Mediapipe is a framework for building multimodal (video, audio, time-series, etc.) applied machine learning pipelines, while CVzone simplifies working with OpenCV. Install both libraries using pip:

```bash
pip install mediapipe
pip install cvzone
```

### Clone the Course Repository
If you haven't done so already, clone the course repository and prepare your environment:

```bash
git clone https://github.com/pannatron/RobodogV_Camp.git
cd RobodogV_Camp
git checkout day4
```
## Day 4 Exercises Overview
On this day, we will focus on the following key applications:

 - Facial Landmarks Detection: Using Mediapipe to detect facial structures.
 - Hand Tracking: Implementing real-time hand tracking with Mediapipe.
 - Object Detection and Tracking: Utilizing CVzone to track objects in video.
 - Advanced Computer Vision Techniques
1. Facial Landmarks Detection
Detect and visualize facial landmarks using Mediapipe:

```bash

import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# Capture video from webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Convert the BGR image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and draw facial landmarks
    results = face_mesh.process(image)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                image, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)

    # Display the image
    cv2.imshow('Facial Landmarks', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
```

