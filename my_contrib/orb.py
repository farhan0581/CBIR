import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('d2.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
orb=cv2.ORB_create(nfeatures=500)
#default was 500
kp=orb.detect(img,None)

kp,des=orb.compute(img,kp)

res=cv2.drawKeypoints(img,kp,None,color=(0,255,0))

cv2.imshow('ORB',res)
cv2.waitKey(0)