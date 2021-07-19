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
arr1 = []
avg=0
while True:

    ret,frame = cap.read()
    if ret ==False:
       break

    frame = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    frame=frame[100:,:,:]
    org=frame
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                cv2.THRESH_BINARY, 11, 7)

    edges = cv2.Canny(th3, 50, 200,None,3)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 100, None, 0, 0)
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

            arr.append(abs(theta * 180 / np.pi - 90))




    cv2.line(org, pt1, pt2, (0, 255, 0), 2, cv2.LINE_AA)
    avg = sum(arr) / (len(arr))
    arr1.append(avg)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(org, str(avg), (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', org)
    cv2.imshow('mask', th3)
    cv2.imshow('edge',edges)

    k = cv2.waitKey(8)
    if k == 27 :
      break

plt.plot(arr1)
plt.show()
o = cv2.waitKey(8)
cap.release()
cv2.destroyAllWindows()


