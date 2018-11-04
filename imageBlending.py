import cv2

img1 = cv2.imread('images/gu.jpeg')
img2 = cv2.imread('images/pais.jpeg')

res1 = cv2.addWeighted(img1,0.7,img2,0.6,0)
res2 = cv2.addWeighted(img2,0.7,img1,0.3,0)
res3 = cv2.addWeighted(img1,0.3,img2,0.7,0)
res4 = cv2.addWeighted(img2,0.3,img1,0.7,0)

cv2.imshow('res1',res1)
cv2.imshow('res2',res2)
cv2.imshow('res3',res3)
cv2.imshow('res4',res4)

cv2.waitKey(0)
cv2.destroyAllWindows()