import cv2 
import numpy as np 

cam = cv2.VideoCapture(0)

pixel = (20, 60, 80)

global Upper 
global Lower

Upper = 0
Lower = 0
black = (0,0,0)

def pickColor(event, x, y, flags, param): 
	global Upper 
	global Lower 

	# If left click is released stores the pixels in a list
	if event == cv2.EVENT_LBUTTONDOWN: 
		pixel = imgHSV[y , x]

		# Adjusting range (+/- 10)
		Upper = np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
		Lower = np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])

		print("Current Value:", pixel , "Lower Value:", Lower, "Upper Value:", Upper)

		# Setting a mask with a value filtered according to the last range set
		imgMASK = cv2.inRange(imgHSV, Lower, Upper)

		# Show the image in a new window 
		cv2.imshow("Mask", imgMASK)

		
while True:
	
	ret, img = cam.read()
	img = cv2.resize(img, (400, 400))

	# Creating a new window
	cv2.namedWindow('HSV')

	# Setting a mouse callback with parameteres to the function pickColor 
	cv2.setMouseCallback('HSV', pickColor)

	# Filtering the image
	imgGAUSS =  cv2.GaussianBlur(img, (7, 7), 0)

	# Converting the image into HSV parameters
	imgHSV = cv2.cvtColor(imgGAUSS, cv2.COLOR_BGR2HSV)

	# Filtering by masks and their respective range 
	maskOrange = cv2.inRange(imgHSV, Lower, Upper)
	# Ellipse around the target 
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))

	# Erosioning the image and then dilating it
	maskOrange_OPEN = cv2.morphologyEx(maskOrange, cv2.MORPH_OPEN, kernel)


	# Dilating the image and then erosioning it
	maskOrange_CLOSE = cv2.morphologyEx(maskOrange, cv2.MORPH_CLOSE, kernel)


	# Finding the contour of the habaneros
	contourOrange, hierarchyOrange = cv2.findContours(maskOrange_CLOSE.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	# Drawing contours around the target in this case the habaneros
	# Orange habaneros
	cv2.drawContours(img, contourOrange, -1, black, 1)
	# Green habaneros

	for contour in range(len(contourOrange)):
		if len(contourOrange[contour]) >= 5:

			ellipse = cv2.fitEllipse(contourOrange[contour])
			cv2.ellipse(img, ellipse, black, 2)
		else: break

	cv2.imshow("s", img)
	cv2.imshow("HSV", imgHSV)
	if (cv2.waitKey(1) & 0xFF) == 27:
		break 

cv2.destroyAllWindows()
