import cv2
import csv
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('test_dataset/d1.jpg')
img2=cv2.imread('test_dataset/d2.jpg')
# fil=open("features.csv","r+")
# filename=csv.writer(fil)

# orb=cv2.ORB_create()
# # filename.writerow(["d1.jpg",""])
# kp1,des1=orb.detectAndCompute(img1,None)#type of kp1 is list
# kp2,des2=orb.detectAndCompute(img2,None)#type of des is numpy array

# np.savetxt(fil,des1,fmt='%d',footer=",")
# np.savetxt(fil,des2,fmt='%d',footer=",")
# #create bf mathcher object
# fil.close()
# fil=open("features.csv","r+")
# filename=csv.reader(fil)
# for row in filename:
# 	print 

# des1=np.array(np.loadtxt('features.csv',dtype='uint8'))
# # print (des1)
# print (des2.dtype)
# print des2
# print des1

# bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

# matches=bf.match(des1,des2)

# matches = sorted(matches, key = lambda x:x.distance)

# img3=cv2.drawMatches(img1,kp1,img2,kp2,matches[:50],None,flags=2)
cv2.imshow('match',img1)

# cv2.waitKey(0)
