import cv2

image=cv2.imread('images/m1.jpg')
cv2.imshow('original',image)
#width height
r=300.0/image.shape[1]
dim=(300,int(image.shape[0]*r))
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)