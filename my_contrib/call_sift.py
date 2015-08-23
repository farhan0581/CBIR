import sift
from pylab import *
from PIL import Image
from numpy import *

imname = "11.jpg"
im1 = array(Image.open(imname).convert("L"))
sift.process_image(imname,"tmp.pgm")
l1,d1 = sift.read_features_from_file("tmp.pgm")
figure()
gray()
sift.plot_features(im1,l1,circle=True)
show()