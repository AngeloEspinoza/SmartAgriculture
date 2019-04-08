#####################################################################################################
#                                      Angelo D. Espinoza V.                                        #
#                                                                                                   #
#     This code counts the shapes of a given colour and throws an approximation of the number of    #
#    					habaneros counted based on the last aspect mentioned  						#
#                                                                                                   #
#    The image input has to be provide in the variable "img" since this program isn't in real       #
#                      If it's necessary should be provide the whole path location                  #
#####################################################################################################


import cv2 
import numpy as np 

# Defining uppers and lowers values 

orangeLower = np.array([2, 243, 213])
greenLower = np.array([0,0,0])
redLower = np.array([0,0,0])

orangeUpper = np.array([22, 263, 293])
greenUpper = np.array([0,0,0])
redUpper = np.array([0,0,0])

black = (0, 0, 0)



def main(): 
	# Importing the image 	
	img = cv2.imread("try.jpg")

	# Filtering the image
	imgGAUSS =  cv2.GaussianBlur(img, (7, 7), 0)

	# Converting the image into HSV parameters
	imgHSV = cv2.cvtColor(imgGAUSS, cv2.COLOR_BGR2HSV)

	# Filtering by masks and their respective 
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
	contourOrange, hierarchyOrange = cv2.findContours(maskOrange_CLOSE.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	contourGreen, hierarchyGreen = cv2.findContours(maskGreen_CLOSE.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	contourRed, hierarchyRed = cv2.findContours(maskRed_CLOSE.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	# Drawing contours around the target in this case the habaneros
	# Orange habaneros
	cv2.drawContours(img, contourOrange, -1, black, 1)
		# Green habaneros
	cv2.drawContours(img, contourGreen, -1, black, 1)
	# Red habaneros
	cv2.drawContours(img, contourRed, -1, black, 1)

	for contour in range(len(contourOrange)):
		if len(contourOrange[contour]) >= 5:

			ellipse = cv2.fitEllipse(contourOrange[contour])
			cv2.ellipse(img, ellipse, black, 2)
		else: break

	print("Number of habaneros is approximately:", len(contourOrange))


	cv2.imwrite("GAUSS4.jpg", img)

main()
