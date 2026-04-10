"""
Pipeline:
1.) Capture video frame
2.) Detect object
3.) Track objects position
4.) Calculate object center
5.) Display control logic based on object position
"""


import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#Capture video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    #Convert colour from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Create HSV bounds for specific colour
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])


    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        ##Debug: print(area)

        #Ignore small objects
        if area > 1000:

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cx = x + w // 2
            cy = y + h // 2

            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            height, width, _ = frame.shape

            left_zone = width // 3
            right_zone = 2 * width // 3

            #Control logic
            if cx < left_zone:
                direction = "LEFT"
            elif cx > right_zone:
                direction = "RIGHT"
            else:
                direction = "FORWARD"

            cv2.putText(frame, direction, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show everything
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)  # Shows what the camera is detecting

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 