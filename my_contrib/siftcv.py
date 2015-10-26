import os
import glob

lis=[]
os.chdir("/home/farhan/project/CBIR/my_contrib/images")
for file in glob.glob("*.jpg"):
   lis.append(file)
print lis