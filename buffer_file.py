
from SimpleCV import *

import time

image  = Image("alpha_B.JPG")

image = image.resize(640,427)

#binimage = image.binarize(180).invert()

binimage = image

binimage.show()

#blobs = foo.findBlobs(maxsize = 5,minsize = 4 )

blobs = binimage.findBlobs()

#blobs[-1].blobImage().show()

for blob in blobs:
	if ( blob.area()<200 and blob.area()>40):
		blob.drawRect(color=Color.BLUE,width=20,alpha = 90)
		print blob.area()
		print blob
		print blob.centroid()
		dl = DrawingLayer((binimage.width,binimage.height))
		blob.drawMaskToLayer(layer = dl)
		#blob.blobImage().show()
		dl.show()
		#binimage.show()
		raw_input()
	else:
		print "Couldn't find, hit enter"

#probably 19 seconds too long ....

#time.sleep(10)



#APIS to hack on
#blobs.coordinates()
#blobs.area()

#150 - 200 pixels 14 MP
