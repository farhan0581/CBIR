import MySQLdb as mdb
import cv2
import csv
import numpy as np
from matplotlib import pyplot as plt
import os,glob
from collections import OrderedDict
from operator import itemgetter
import itertools

def insert_data():
	con=mdb.connect('localhost','root','','cbir')
	cur=con.cursor()
	os.chdir("/home/farhan/project/CBIR/my_contrib/images")
	for fil in glob.glob("*.jpg"):
		img=cv2.imread('/home/farhan/project/CBIR/my_contrib/images/'+fil)
		orb=cv2.ORB_create()
		kp,desc=orb.detectAndCompute(img,None)
		byte=desc.dumps()
		cur.execute("""insert ignore into prop(name,des) values(%s,%s)""",(fil,byte))
		con.commit()

def matching():
	in_img=raw_input("please enter the query image")
	query_img=cv2.imread('images/'+in_img)
	orb=cv2.ORB_create()
	bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
	kp,des=orb.detectAndCompute(query_img,None)
	con=mdb.connect('localhost','root','','cbir')
	cur=con.cursor()
	query="select name,des from prop where name like '%jpg'"
	cur.execute(query)
	rows=cur.fetchall()
	res_dict={}
	for row in rows:
		val=0
		dess=np.ma.loads(row[1])
		matches=bf.match(des,dess)
		matches = sorted(matches, key = lambda x:x.distance)
		for dis in matches[:15]:
			val+=dis.distance
		res_dict[row[0]]=val
	# print res_dict
	d = OrderedDict(sorted(res_dict.items(), key=itemgetter(1)))
	x = itertools.islice(d.items(), 0, 5)
	for value in x:
		to_show=cv2.imread('images/'+value[0])
		cv2.imshow('match',to_show)
		cv2.waitKey(0)
	


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
# insert_data()create table testing(id int primary key not null,name varchar(40))
matching()




