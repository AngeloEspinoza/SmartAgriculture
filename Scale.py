#####################################################################################################
#                                      Angelo D. Espinoza V.                                        #
#                                                                                                   #
#   This code was made with the purpose of facilitating at the moment of choosing a range between	#
# 	colors for the function cv2.cvtColor() in real time, this was code was based in a code that		#	
#						can be found in the next link: https://bit.ly/2D5YM0s 						#
#			  																						#
#                                                                                                   #
#    After compiling the program 2 windows will be opened, one with the RGB window and other with   #
#    HSV window, in order to print out the range values you should left-click on the HSV window     #
# 	then another window with the mask based on the range provided will be opened, and a message 	#
# 	in console with 3 arrays, the first is the actual pixels, the second array with a -10 range 	#
# 	and finally the third array with a +10 range, the last two should be taken in consideration 	#
#					at the moment of putting in the function cv2.cvtColor() 						#
#####################################################################################################

import cv2 
import numpy as np 

# Initializing the camera #0
cam = cv2.VideoCapture(0)

# Just a value
pixel = (20, 60, 80)

#####################################################################################
# The purpose of this function is to do each time a left click is pressed a windows #
#  							it prints out a range based  							# 
#####################################################################################

def pickColor(event, x, y, flags, param): 
	# If left click is released stores the pixels in a list
	if event == cv2.EVENT_LBUTTONDOWN: 
		pixel = imgHSV[y , x]

		# Adjusting range (+/- 10)
		Upper = np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
		Lower = np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])

		print("Current Value:", pixel , "Lower Value:", Lower, "Upper Value", Upper)

		# Setting a mask with a value filtered according to the last range set
		imgMASK = cv2.inRange(imgHSV, Lower, Upper)

		# Show the image in a new window 
		cv2.imshow("Mask", imgMASK)

# Constant loop 
while True: 

	# Reading pixel by pixel of the camera 
	ret, img = cam.read()
	
	# Creating a new window
	cv2.namedWindow('HSV')

	# Setting a mouse callback with parameteres to the function pickColor 
	cv2.setMouseCallback('HSV', pickColor)

	# Converting from HSV to BGR 
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Displaying the image 
	cv2.imshow("HSV", imgHSV)
	cv2.imshow("BGR", img)

	# If ESC pressed closes all the windows
	if (cv2.waitKey(1) & 0xFF) == 27:
		break
	else: pass 
cv2.destroyAllWindows()
