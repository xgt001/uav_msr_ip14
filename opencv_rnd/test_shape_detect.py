__author__ = 'ganesh'



__author__ = 'ganesh'


import cv2
import numpy as np

# TODO: loop through folder files


filename = "alpha_N.JPG"
image = cv2.imread(filename)
newx,newy = image.shape[1]/6,image.shape[0]/6 #new size (w,h)
img = cv2.resize(image,(newx,newy))

img_sav = img
# CODE: Resize Image Toggle
# cv2.imshow("resize image",img)
# cv2.waitKey(0)

circle = cv2.imread("circle.jpg")


img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

image_circle = cv2.cvtColor(circle,cv2.COLOR_RGB2GRAY)

retval, threshold = cv2.threshold(img,170,200,cv2.THRESH_BINARY_INV)

# ret1, thresh_circ = cv2.threshold(image_circle,cv2.THRESH_BINARY)
#
# cv2.imshow("threshold",threshold)
# cv2.waitKey(0)

# contours,hierarchy = cv2.findContours(threshold,1,2)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

shape_circle, hier2 = cv2.findContours(image_circle,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

contours.sort(key=cv2.contourArea, reverse=True)

#DOCUMENTATION
#


for i in range(0,100,1):

    ret = cv2.matchShapes(contours[i],shape_circle,1,0.0)
    if cv2.contourArea(contours[i]) < 300 and cv2.contourArea(contours[i]) > 50 and ret < 5 and ret > 0 :

        print "match:"; print ret
        print "Area:"; print cv2.contourArea(contours[i])
        cv2.drawContours(img_sav,contours,i,(0,255,0),1)
        x,y,w,h = cv2.boundingRect(contours[i])
        cv2.rectangle(img_sav,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("test",img_sav)
        cv2.imwrite("blob"+str(i)+'.png', img_sav[y:y+h,x:x+w])
        cv2.waitKey(0)
