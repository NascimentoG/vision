import cv2
import numpy as np
import matplotlib as plt

def main():
	
	while 1:

		img = cv2.imread('chocolate.jpeg')

		#res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

		#OR

		height, width = img.shape[:2]
		res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

		cv2.imshow("Original",img)
		cv2.imshow("Scaling",res)

		if cv2.waitKey(1) == 27:
			break

	cv2.destroyAllWindows()
	cap.release()

if __name__ == '__main__':
	main()