import cv2
import numpy as np
image = cv2.imread("/home/farhan/Desktop/1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
(kps, descs) = sift.detectAndCompute(gray, None)
# print("# kps: {}, descriptors: {}".format(len(kps), descs.shape))
#  # kps: 274, descriptors: (274, 128)
# surf = cv2.xfeatures2d.SURF_create()
# (kps, descs) = surf.detectAndCompute(gray, None)
# print("# kps: {}, descriptors: {}".format(len(kps), descs.shape))
# # kps: 393, descriptors: (393, 64)
# img = cv2.imread('11.jpg')
# gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# sift = cv2.xfeatures2d.SIFT_create()
# kp = sift.detect(gray,None)

# img=cv2.drawKeypoints(gray,kp,img)

cv2.imwrite('sift_keypoints.jpg',img)
print descs