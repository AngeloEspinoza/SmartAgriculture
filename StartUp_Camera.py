import cv2 
import pyrealsense2 as rs

cam = cv2.VideoCapture(2)

# while True: 

#     ret, img = cam.read()
#     img = cv2.resize(img,(400,400))

#     if (cv2.waitKey(1) & 0xFF) == 27:
#         break
#     else: 
#         pass

#     cv2.imshow("Camera Window", img)

