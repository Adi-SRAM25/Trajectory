import cv2
import numpy as np
cap = cv2.VideoCapture('detect.mp4')
while True:
    _,frame = cap.read()
    nframe = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    gray = cv2.cvtColor(nframe,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize=3)
    cv2.imshow("canny",edges)
    lines = cv2.HoughLines(edges,1,np.pi/180,100)

    for line in lines:
        rho,theta = line[0]
        print("theta : ")
        print(theta)
        a = np.cos(theta)
        b=np.sin(theta)
        x0=a*rho
        y0=b*rho
        x1 = int(x0+ 1000*(-b))
        y1 = int(y0 + 1000*a)
        x2 = int (x0-1000*(-b))
        y2 = int (y0-1000*a)
        cv2.line(nframe,(x1,y1),(x2,y2),(255,255,0),2)
        cv2.imshow("frame",nframe)

    k=cv2.waitKey(8)
    if k ==27:
        break

cap.release()
cv2.destroyAllWindows()

