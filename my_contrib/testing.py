import cv2
import numpy as np
import os
img=np.zeros((512,512,3),np.uint8)
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imwrite('cnjd.jpg',img)
cv2.imshow('bla',img)
# img = cv2.imread('11.jpg')
# gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# # sift = cv2.xfeatures2d.SIFT_create()
# s=cv2.xfeatures2d.SIFT_create()
# kp = sift.detect(gray,None)

# img=cv2.drawKeypoints(gray,kp)

# cv2.imwrite('sift_keypoints.jpg',img)
