import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def nothing(x):
    pass
frame = 0
i=0
cap = cv2.VideoCapture('ball.mp4')
#cv2.namedWindow('tracking')
cv2.createTrackbar('LH','tracking',0,255,nothing)
cv2.createTrackbar('LS','tracking',0,255,nothing)
cv2.createTrackbar('LV','tracking',0,255,nothing)
cv2.createTrackbar('UH','tracking',255,255,nothing)
cv2.createTrackbar('US','tracking',255,255,nothing)
cv2.createTrackbar('UV','tracking',255,255,nothing)
mat1 = 0
x=[]
y=[]
yp=[]

while True:

    ret,frame = cap.read()
    if ret ==False:
      break

    frame = frame[150:,:,:]
    frame = cv2.resize(frame, (360, 640))
    mg = frame
    s = frame.shape


    lh = cv2.getTrackbarPos('LH','tracking')
    ls = cv2.getTrackbarPos('LS', 'tracking')
    lv = cv2.getTrackbarPos('LV', 'tracking')

    uh = cv2.getTrackbarPos('UH', 'tracking')
    us = cv2.getTrackbarPos('US', 'tracking')
    uv = cv2.getTrackbarPos('UV', 'tracking')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   # l_b = np.array([lh,ls,lv])
    #u_b = np.array([uh,us,uv])

    l_b = np.array([0, 51, 120])
    u_b = np.array([90, 255, 255])

    mask = cv2.inRange(hsv,l_b,u_b)
    lower_red = np.array([0, 81, 47])
    upper_red = np.array([49, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    maskh = mask + mask1

    kernel_erode = np.ones((4, 4), np.uint8)
    eroded_mask = cv2.erode(maskh, kernel_erode, iterations=1)
    kernel_dilate = np.ones((6, 6), np.uint8)
    dilated_mask = cv2.dilate(eroded_mask, kernel_dilate, iterations=1)
    res=cv2.bitwise_and(frame,frame,mask=dilated_mask)

    frame = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    th3 = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                cv2.THRESH_BINARY, 11, 7)

    edges = cv2.Canny(th3, 50, 200, None, 3)

    #cv2.imshow('frame',th3)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    #cv2.imshow('ed',edges)

    M = cv2.moments(edges)

    if M["m00"] !=0 :

      cX = int(M["m10"] / M["m00"])
      cY = int(M["m01"] / M["m00"])
      x.append(cX)
      y.append(cY)
      yp.append(s[0]-cY)

      cv2.circle(mg, (cX, cY), 15, (0, 255,255 ), 2)
      cv2.putText(mg, "BALL", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)



    for i in range(1,len(x)):
        cv2.line(mg,(x[i-1],y[i-1]),(x[i],y[i]),(0,0,255),2)
        cv2.circle(mg, (x[i-1],y[i-1]), 2, (0, 255,255 ), 2)
        cv2.imshow("Image", mg)
        cv2.imshow("mask",dilated_mask)

    (_, contours,_) = cv2.findContours( dilated_mask , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(mg, (x, y), (x + w, y + h), (0, 255, 0), 2)

    k = cv2.waitKey(500)
    if k == 27 :
        break

plt.plot(x,yp)
plt.show()
cap.release()
cv2.destroyAllWindows()