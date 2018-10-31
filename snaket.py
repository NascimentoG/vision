import cv2
import numpy as np 
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour

def main():
	
	cap = cv2.VideoCapture(0)

	if cap.isOpened():
		ret, frame = cap.read()
	else:
		ret = False

	while ret:

		ret, frame = cap.read()

		img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		s = np.linspace(0, 2*np.pi, 400)
		x = 220 + 100*np.cos(s)
		y = 100 + 100*np.sin(s)
		init = np.array([x, y]).T

		snake = active_contour(gaussian(img, 3),
                  		     init, alpha=0.015, beta=10, gamma=0.001)
		cv2.imshow("Snaking",frame)

		if cv2.waitKey(1) == 27:
			break

	cv2.destroyAllWindows()
	cap.release()

if __name__ == "__main__":
	main()
