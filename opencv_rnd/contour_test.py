import cv2
import numpy as np

# TODO: loop through folder files


filename = "alpha_N.JPG"
image = cv2.imread(filename)
newx,newy = image.shape[1]/4,image.shape[0]/4 #new size (w,h)
img = cv2.resize(image,(newx,newy))

img_sav = img
# CODE: Resize Image Toggle
# cv2.imshow("resize image",img)
# cv2.waitKey(0)


img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

retval, threshold = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
#
# cv2.imshow("threshold",threshold)
# cv2.waitKey(0)

contours,hierarchy = cv2.findContours(threshold,1,2)
#
# for cnt_detect in contours:
#     area = cv2.contourArea(cnt_detect)
#     if area > 20:
#         # (x,y),radius = cv2.minEnclosingCircle(cnt_detect)
#         # center = (int(x),int(y))
#         # radius = int(radius)
#         # threshold = cv2.circle(threshold,center,radius,(0,255,0),2)
#         # cv2.drawContours(threshold,cnt_detect,)
#
#         print area
#         cv2.drawContours(img_sav,cnt_detect, 0, (0,255,0), 7)
#         cv2.imshow("test",img_sav)
#         cv2.waitKey(0)
#         draw individual contours
# contour filtering



#draw all contours
cv2.drawContours(img_sav, contours, -1, (0,255,0), 3)

# print contours

# print area




#fair enough till here
#
# contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#
#
# print len(contours)
#
# cunt = contours[0]
#
# print len(cunt)
#
# cv2.drawContours(img,cunt,-1,(0,255,0),-1)
# #to keep the window afloat
#

cv2.imshow("test",img_sav)

cv2.waitKey(0)
cv2.destroyAllWindows()

