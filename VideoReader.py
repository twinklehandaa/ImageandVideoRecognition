import numpy as np
import cv2

cap = cv2.VideoCapture('C:/Users/hp/Downloads/Ex_Files_Deep_Learning_OpenCV/Exercise Files/images/shore.mp4')

if cap.isOpened() == False:
    print('Cannot open file or video stream')

while True:
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
