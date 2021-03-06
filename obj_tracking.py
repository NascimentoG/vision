import cv2
import numpy as np 

def main():
	
	cap = cv2.VideoCapture(0)

	if cap.isOpened():
		ret, frame = cap.read()
	else:
		ret = False

	while ret:

		ret, frame = cap.read()

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		#Blue Color
		low_blue = np.array([100,50,50])
		high_blue = np.array([140,255,255])

		#Green Color
		low_green = np.array([40,50,50])
		high_green = np.array([80,255,255])

		#Red Color
		low_red = np.array([110,150,0])
		high_red = np.array([200,255,255])

		image_maskB = cv2.inRange(hsv,low_blue,high_blue)
		outputB = cv2.bitwise_and(frame,frame, mask = image_maskB)

		image_maskG = cv2.inRange(hsv,low_green,high_green)
		outputG = cv2.bitwise_and(frame,frame, mask = image_maskG)

		image_maskR = cv2.inRange(hsv,low_red,high_red)
		outputR = cv2.bitwise_and(frame,frame, mask = image_maskR)

		output1 = cv2.add(outputB,outputR,outputG)
		output2 = outputB+outputG+outputR
		#m = np.array([image_maskR,image_maskG,image_maskB])
		#m = np.swapaxes(m, 0,2)
		#m = np.swapaxes(m, 0,1)
		#print(m.shape)
		#print(frame.shape)

		#o = cv2.bitwise_and(frame,m)
		
		cv2.imshow("Original Webcam Feed",frame)
		cv2.imshow("BRG segmentation", output2)
		cv2.imshow("BGR segmentation with opencv",output1)
		#cv2.imshow("Blue color Tracking",outputB)
		#cv2.imshow("Green color Tracking",outputG)
		#cv2.imshow("Red color Tracking",outputR)

		if cv2.waitKey(1) == 27:
			break

	cv2.destroyAllWindows()
	cap.release()

if __name__ == "__main__":
	main()
