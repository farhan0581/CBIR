# script to mask the required coloured region from a image
import cv2
import numpy as np
import matplotlib.pyplot as pl

img=cv2.imread('12.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

low=np.array([204,193,255])
high=np.array([11,0,101])

mask=cv2.inRange(img_hsv,high,low)
result=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("vcdv",result)
cv2.waitKey(0)
