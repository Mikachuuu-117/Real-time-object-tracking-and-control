# OpenCV Object Tracking System

A real time computer vision system that was developed uing Python and OpenCV. The system tracks coloured objects using HSV colour segmentation and determines their positions relative to the camera frame and outputs simple movement logic.

The system was designed for use inn robotics and autonomous systems where visual feedback can be used for navigation or tracking.

## Demo
![Demo](Assets/Object-tracking-demo.gif)

## Features
- Real time video processing
- HSV colour based object detection
- Contour detection and center tracking
- Visual debugging overlays:
    - Bounding boxes
    - Object center point
- Basic navigation loguc display

## How it works

- Live video is captured from webcam
- Applies HSV thresholding to detect target object
- Uses contour detection to find object position
- Determines objects position relative to frame center
- Outputs control logic based on object position in frame in real time

## Technologies Used
- Python
- OpenCV
- NumPy

## Run
- pip install -r requirements.txt
- python main.py
- Put a red object in frame and it will be tracked
- To change colour to be tracked adjust HSV values in code accordingly
- To exit frame press 'q'

