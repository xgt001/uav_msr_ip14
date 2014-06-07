
def image_extractor(name):

	binimage = Image(name)

	if binimage.height == 3072:	

		print "Hi Testing \n"
	else:
		binimage = binimage.rotateRight()


	#image = image.resize(640,427)

	#image = image.scale(0.22)

	#binimage = image.binarize(180).invert()

	blobs = binimage.findBlobs()

	counter = 0

	for blob in blobs:
		if ( blob.area()<4700 and blob.area()>1800):
			blob.drawRect(color=Color.BLUE,width=20,alpha = 90)
			print blob.area()
			print blob
			print blob.centroid()
			binimage.crop(blob).show()
			#update for path needed, make it automatically pickup
			save_path =  "I:\\Editha\\detects\\"+"blob-"+str(counter)+".JPG"
			counter +=1
			binimage.crop(blob).save(save_path)
			#raw_input()
			
		'''
		#DEBUG 
		else:
			print "Couldn't find, hit enter"
		'''


if __name__ == '__main__':

	from SimpleCV import *

	import time,os,sys

	path = "I:\\Editha\\all"
	files = os.listdir(path)

	for file in files:
		image_extractor("I:\\Editha\\all\\"+file)





