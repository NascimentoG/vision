import cv2 as cv

img1 = cv.imread('images/jujuba.jpeg')
img2 = cv.imread('images/gu.jpeg')

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

cv.imshow('whaaaat',roi)

img2gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

cv.imshow('mask_inv',mask_inv)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
cv.imshow('img1_bg',img1_bg)
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
cv.imshow('img2_fg',img2_fg)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img2[0:rows, 0:cols ] = dst

cv.imshow('res',img2)
cv.waitKey(0)
cv.destroyAllWindows()