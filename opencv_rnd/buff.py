import cv2
import numpy as np



img = cv2.imread('alpha_o.JPG',1)
scaledown = cv2.resize(img,(0,0),fx=0.25,fy=0.25)


color_space = cv2.cvtColor(scaledown,cv2.COLOR_RGB2HSV)

sift = cv2.SIFT(7)

kp = sift.detect(color_space,None)

scaledown = cv2.drawKeypoints(color_space,kp)



cv2.imshow('image',scaledown)
cv2.waitKey(0)
cv2.destroyAllWindows()

__author__ = 'ganesh'
