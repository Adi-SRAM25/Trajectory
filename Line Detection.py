import cv2
import numpy as np
import math
import statistics
import matplotlib.pyplot as plt

def nothing (x):
    pass
cap = cv2.VideoCapture('detect.mp4')
i = 0
md = 0
arr = []
while True:

    ret,frame = cap.read()
    if ret ==False:
      break

    frame = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)

    blur = cv2.GaussianBlur(frame, (5, 5), 0)

    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #l_b = np.array([30, 0, 0])
    #u_b = np.array([255,255,255])

    #mask =  cv2.inRange(hsv,l_b,u_b)

    #kernel_erode = np.ones((4, 4), np.uint8)
    #eroded_mask = cv2.erode(mask, kernel_erode, iterations=1)
    #kernel_dilate = np.ones((6, 6), np.uint8)
    #dilated_mask = cv2.dilate(eroded_mask, kernel_dilate, iterations=1)

    edges = cv2.Canny(frame, 50, 200)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150, None, 0, 0)


    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))


            arr.append(int(abs(theta*180/np.pi -90)) )

    md = statistics.mode(arr[-10:-1])
    print(md)
    cv2.line(frame, pt1, pt2, (0, 255, 0), 2, cv2.LINE_AA)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, str(md), (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('edge',edges)

    k = cv2.waitKey(8)
    if k == 27 | ret ==False:
      break

plt.plot(arr)
plt.show()
u = cv2.waitKey(5)
cap.release()
cv2.destroyAllWindows()