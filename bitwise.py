import cv2
import numpy as np

img2 = cv2.imread('lena.jpg')
b,g,r = img2.shape
img1 = np.zeros((b,g,r),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
#img1 = cv2.add(img1,100)
bitAnd =cv2.bitwise_not(img2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('bitwise',bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()