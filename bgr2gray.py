import cv2
import numpy as np 

capture = cv2.VideoCapture(0)

while(1):
	_, frame = capture.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	cv2.imshow('Real',frame)
	cv2.imshow('Cinza',gray)
	cv2.imshow('HSV',hsv)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()