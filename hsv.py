import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def nothing(x):
    pass
frame = 0
i=0
cap = cv2.VideoCapture('ball.mp4')
cv2.namedWindow('tracking')
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
i=0
while True:
    if i<=15:
      ret,frame = cap.read()

    i+=1
    frame = cv2.resize(frame, (360, 640))
    mg = frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('LH','tracking')
    ls = cv2.getTrackbarPos('LS', 'tracking')
    lv = cv2.getTrackbarPos('LV', 'tracking')

    uh = cv2.getTrackbarPos('UH', 'tracking')
    us = cv2.getTrackbarPos('US', 'tracking')
    uv = cv2.getTrackbarPos('UV', 'tracking')


    l_b = np.array([lh, ls, lv])
    u_b = np.array([uh, us, uv])
    #l_b = np.array([0, 51, 120])
    #u_b = np.array([90, 255, 255])
    mask = cv2.inRange(hsv,l_b,u_b)


    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask', maskh)
    cv2.imshow('res', res)


    k = cv2.waitKey(100)
    if k == 27 :
        break

cap.release()
cv2.destroyAllWindows()