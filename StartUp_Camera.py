####################################################################################################
#                                      Angelo D. Espinoza V.                                       #
#                                                                                                  #
#     With this code the camera RGB of the Intel RealSense R200 can be started up                  #
#                                                                                                  #   
#    It is necessary just to prove that the camera initializes first with the app of the computer  #
####################################################################################################

# Importing the library of OpenCV
import cv2 

# Defining which camera that will be used in this case the 2
# By default the argument should be 0
# The RGB camera of the  R200 is the #2 
cam = cv2.VideoCapture(2)

# Constant loop 
while True: 
    
    # Reading the pixels of the camera and putting the information into two variables
    ret, img = cam.read()
    
    # Resizing the image by 400 x 400 
    img = cv2.resize(img,(400,400))

    # If ESC pressed closes all the windows
    if (cv2.waitKey(1) & 0xFF) == 27:
        break
    else: 
        pass

    # Projecting the image     
    cv2.imshow("Camera Window", img)


# Making sure all windows closed
cv2.destroyAllWindows()
    
