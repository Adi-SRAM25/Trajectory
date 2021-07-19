import numpy as np
import cv2

#img = cv2.imread('lena.jpg',1)
img = np.zeros([512,512,3], np.uint8)

img = cv2.arrowedLine(img, (0,255) , (255,255),  (255,0,0), 5)
img = cv2.rectangle(img, (384,0),(510,128),(0,255,0),5)
img = cv2.circle(img, (255,255),63,(0,0,255),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'openCV', (0,255),font,4,(255,255,255),10,cv2.LINE_AA )
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()