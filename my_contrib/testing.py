import MySQLdb as mdb
import cv2
import csv
import numpy as np
from matplotlib import pyplot as plt
import os,glob

def insert_data():
	con=mdb.connect('localhost','root','','cbir')
	cur=con.cursor()
	os.chdir("/home/farhan/project/CBIR/my_contrib/images")
	for fil in glob.glob("*.jpg"):
		img=cv2.imread('/home/farhan/project/CBIR/my_contrib/images/'+fil)
		orb=cv2.ORB_create()
		kp,desc=orb.detectAndCompute(img,None)
		byte=desc.dumps()
		cur.execute("""insert into prop(name,des) values(%s,%s)""",(fil,byte))
		con.commit()

def matching():
	query_img=cv2.imread('images/d1.jpg')
	orb=cv2.ORB_create()
	bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
	kp,des=orb.detectAndCompute(query_img,None)
	con=mdb.connect('localhost','root','','cbir')
	cur=con.cursor()
	query="select des from prop"
	cur.execute(query)
	rows=cur.fetchall()
	for row in rows:
		dess=np.ma.loads(row[0])
		matches=bf.match(des,dess)
		matches = sorted(matches, key = lambda x:x.distance)
		

img1=cv2.imread('images/d1.jpg')
img2=cv2.imread('images/d2.jpg')
img4=cv2.imread('images/d3.jpg')
orb=cv2.ORB_create()
kp1,des1=orb.detectAndCompute(img1,None)#type of kp1 is list
kp2,des2=orb.detectAndCompute(img2,None)#type of des is numpy array
kp3,des3=orb.detectAndCompute(img4,None)#type of des is numpy array

bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches1=bf.match(des1,des2)
matches2=bf.match(des1,des3)
matches1 = sorted(matches1, key = lambda x:x.distance)
matches2 = sorted(matches2, key = lambda x:x.distance)
for point in matches1:
	print point.distance
print 'vxcjbvxjhvbxjcbvjxchbvjcxhbv'
for point in matches2:
	print point.distance
# img3=cv2.drawMatches(img1,kp1,img2,kp2,matches[:50],None,flags=2)
# byte_array=des1.dumps()
# # np.des1.dumps()
# # print type(st)
# # print st

# query="select des from prop where id=19"
# # cur.execute("""insert into prop(des) values (%s)""",(byte_array))
# cur.execute(query)
# rows=cur.fetchall()
# fil=""
# for row in rows:
#  	des11=np.ma.loads(row[0])
#  	# des12=(des11).dumps()
#  	print row[0]
#  	# des11=row[0].astype(dtype='uint8')
# con.commit()
# matches=bf.match(des11,des2)
# matches = sorted(matches, key = lambda x:x.distance)
# img3=cv2.drawMatches(img1,kp1,img2,kp2,matches[:50],None,flags=2)
# cv2.imshow('match',img3)
# cv2.waitKey(0)
# matching()
