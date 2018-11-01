import cv2
import numpy as np

img = cv2.imread('lucasw.jpeg',0)
rows,cols = img.shape

# Matrix de translação os parâmetros da terceira coluna é para transladar [[1,0,tx],[0,1,ty]]
M = np.float32([[1,0,300],[0,1,150]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()