import cv2
import numpy as np

#events =  [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_events (event, x,y, flags, param) :
    if event == cv2.EVENT_LBUTTONDOWN:
        b = int(img[y, x, 0])
        g = int(img[y, x, 1])
        r = int(img[y, x, 2])
        cv2.circle( img ,(x,y) , 5, (b,g,r),-1)
        #points.append((x,y))
        #if len (points) >=2:
            #cv2.line(img,points[-1],points[-2],(255,0,0),5)
        mycolor = np.zeros((512,512,3),np.uint8)
        mycolor[:]= [b,g,r]

        cv2.imshow('color', mycolor)



img = np.zeros((512,512,3), np.uint8)
#img = cv2.imread('lena.jpg')
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image', click_events)

cv2.waitKey(0)
cv2.destroyAllWindows()