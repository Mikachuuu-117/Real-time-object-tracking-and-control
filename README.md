# Real-time object tracking and control

Software that uses real time computer vision to implement a real-time object tracking system sllowing control logic based on objects detected position. Designed for autonomous and robotics applications where visual feedback is used to determine th ebehavior of a system.

## How it works

- Live video is captured
- Detects and tracks a target object based on set HSV values
- Determines objects position relative to frame center
- Outputs control logic based on object opsition in frame

## Features
- Real-time video processing
- Object center based position estimation
- Visual debugging overlay (Bounding box, center point)

## Run
- pip install -r requirements.txt
- python main.py
- Put a red object in frame and it will be tracked
- To change colour to be tracked adjust HSV values in code acordingly
- To exit frame press 'q'
