#####################################################################################################
#                                      Angelo D. Espinoza V.                                        #
#                                                                                                   #
#     This code can at certain point recognize the colours of the three different types of          #
#    habanero pepper (red, green, orange/yellow) and also depicts the name of each one in real time #
#                                                                                                   #
#    It is necessary to prove that the camera initializes first with the app of the computer        #
#                           before compiling this program in Python                                 #
#####################################################################################################

import cv2 
import numpy as np 

# Defining which camera that will be used in this case the 2
# By default the argument should be 0
# The RGB camera of the  R200 is the #2 
cam = cv2.VideoCapture(0)

# Orange Habanero Pepper
# Defining orange colour bounds  
orangeLower = np.array([7, 187, 183])
orangeUpper = np.array([27, 207, 255])

# Green Habanero Pepper
# Defining green colour bounds
greenLower = np.array([32, 174, 104])
greenUpper = np.array([52, 194, 184])

# Red Habanero Pepper
# Defining reed colour bounds
redLower = np.array([7, 214, 114])
redUpper = np.array([17, 234, 194]) 

# Defininf colours in BGR
black = (0, 0, 0)
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

# Font text 
font = cv2.FONT_HERSHEY_SIMPLEX

# Constant loop 
while True: 
    
    # Reading the pixels of the camera and putting the information into two variables
    ret, img = cam.read()
    
    # Resizing the image by 400 x 400 
    img = cv2.resize(img,(400,400))

    # Filtering the image by reducing the noise
    imgGAUSS = cv2.GaussianBlur(img, (7, 7), 0)

    # Taking the image with less noise and convertin it to HSV
    imgHSV = cv2.cvtColor(imgGAUSS, cv2.COLOR_BGR2HSV)

    # Masks of the three habanero color
    maskOrange = cv2.inRange(imgHSV, orangeLower, orangeUpper)
    maskGreen = cv2.inRange(imgHSV, greenLower, greenUpper)
    maskRed = cv2.inRange(imgHSV, redLower, redUpper)

    # Ellipse around the target 
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))

    # Erosioning the image and then dilating it
    maskOrange_OPEN = cv2.morphologyEx(maskOrange, cv2.MORPH_OPEN, kernel)
    maskGreen_OPEN = cv2.morphologyEx(maskGreen, cv2.MORPH_OPEN, kernel)
    maskRed_OPEN = cv2.morphologyEx(maskRed, cv2.MORPH_OPEN, kernel) 

    # Dilating the image and then erosioning it
    maskOrange_CLOSE = cv2.morphologyEx(maskOrange, cv2.MORPH_CLOSE, kernel)
    maskGreen_CLOSE = cv2.morphologyEx(maskGreen, cv2.MORPH_CLOSE, kernel)
    maskRed_CLOSE = cv2.morphologyEx(maskRed, cv2.MORPH_CLOSE, kernel) 

    # Finding the contour of the habaneros
    contourOrange, hierarchyOrange = cv2.findContours(maskOrange_CLOSE.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contourGreen, hierarchyGreen = cv2.findContours(maskGreen_CLOSE.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contourRed, hierarchyRed = cv2.findContours(maskRed_CLOSE.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Drawing contours around the target in this case the habaneros
    # Orange habaneros
    cv2.drawContours(img, contourOrange, -1, black, 1)
    # Green habaneros
    cv2.drawContours(img, contourGreen, -1, black, 1)
    # Red habaneros
    cv2.drawContours(img, contourRed, -1, black, 1)

    # Looping around the recognized colours contours and then drawing an ellipse with certain colour

    for i in range(len(contourOrange)):
        if len(contourOrange[i]) >= 5:
            ellipse_1 = cv2.fitEllipse(contourOrange[i])
            cv2.ellipse(img, ellipse_1, blue, 2)

            # Taking the position in a tuple and converting it to a list
            orangeListEllipse = list(ellipse_1[0])

            # Taking the position X and Y of the target 
            orangeEllipseinX = int(orangeListEllipse[0])
            orangeEllipseinY = int(orangeListEllipse[1])
            
            # Writing the text "Orange Habanero" following the image 
            cv2.putText(img, 'Orange Habanero',(orangeEllipseinX, orangeEllipseinY) , font, 0.5, black, 1, cv2.LINE_AA)
        else: break 

    for i in range(len(contourGreen)):
        if len(contourGreen[i]) >= 5:
            ellipse_2 = cv2.fitEllipse(contourGreen[i])
            cv2.ellipse(img, ellipse_2, red, 2)

            # Taking the position in a tuple and converting it to a list
            greenListEllipse = list(ellipse_2[0])

            # Taking the position X and Y of the target 
            greenEllipseinX = int(greenListEllipse[0])
            greenEllipseinY = int(greenListEllipse[1])
            
            # Writing the text "Green Habanero" following the image 
            cv2.putText(img, 'Green Habanero',(greenEllipseinX, greenEllipseinY) , font, 0.5, black, 1, cv2.LINE_AA)
        else: break

    for i in range(len(contourRed)):
        if len(contourRed[i]) >= 5:
            ellipse_3 = cv2.fitEllipse(contourRed[i])
            cv2.ellipse(img, ellipse_3, green, 2)

            # Taking the position in a tuple and converting it to a list
            redListEllipse = list(ellipse_3[0])

            # Taking the position X and Y of the target 
            redEllipseinX = int(redListEllipse[0])
            redEllipseinY = int(redListEllipse[1])
            
            # Writing the text "Red Habanero" following the image 
            cv2.putText(img, 'Red Habanero',(redEllipseinX, redEllipseinY) , font, 0.5, black, 1, cv2.LINE_AA)       
        else: break

    # If ESC pressed closes all the windows
    if (cv2.waitKey(1) & 0xFF) == 27:
        break
    else: pass

    # Projecting the image     
    cv2.imshow("Camera Window", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("", imgGAUSS)
    #cv2.imshow("", maskOrange_CLOSE)


# Making sure all windows closed
cv2.destroyAllWindows()
