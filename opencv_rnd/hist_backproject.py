import cv2
import numpy as np
#
#
# roi = cv2.imread('blob_R.jpg')
# hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

target = cv2.imread('alpha_D.JPG')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

# # calculating object histogram. From StackOverflow
# An image histogram measures the distribution of colour (and brightness) of the pixels in an image.
# If you take an image and identify a region of interest eg. a hand, and calculate the histogram of the pixels in that object.
#
# Then take that histogram and a second image and essentially reverse the process - you pick the pixels in the second image that match the histogram from the first.
# It's this reverse process that gives it the name back-projection.
#
# You then make the assumption that areas of the image in the second image that have the same colour distribution as an object in the first image are an
# image of the same (or similar) object.

#hue varies from 0 to 256, saturation from 0 to 180

source_image_histogram = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )
#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

# normalize histogram and apply backprojection
# cv2.normalize(source_image_histogram,source_image_histogram,0,255,cv2.NORM_MINMAX)

#DONOT normalize the image, destroys the blob due to irregularities
dst = cv2.calcBackProject([hsvt],[0,1],source_image_histogram,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disc,dst)

# threshold and binary http://opencvpython.blogspot.in/2013/05/thresholding.html
ret,thresh = cv2.threshold(dst,50,255,0)
# cv2.threshold(src, thresh, maxval, type[, dst])  retval, dst



thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)

res = np.vstack((target,res))
cv2.imwrite('res.jpg',res)