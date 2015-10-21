from PIL import Image
from numpy import *
import sift

sift.process_image('tmp.pgm', 'tmp.key')
l1,d1 = sift.read_features_from_file('tmp.key')
im = array(Image.open('tmp.pgm'))
sift.plot_features(im,l1)
# import sift
# from pylab import *
# from PIL import Image
# from numpy import *
# import sift

# imname = "11.jpg"
# im1 = array(Image.open(imname).convert("L"))
# sift.process_image(imname,"11.sift")
# l1,d1 = sift.read_features_from_file("11.sift")
# figure()
# gray()
# sift.plot_features(im1,l1,circle=True)
# show()