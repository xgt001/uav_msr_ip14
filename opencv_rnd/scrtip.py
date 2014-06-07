import cv2
filename = "alpha_o.JPG"
oriimage = cv2.imread(filename)
newx,newy = oriimage.shape[1]/4,oriimage.shape[0]/4 #new size (w,h)
newimage = cv2.resize(oriimage,(newx,newy))
cv2.imshow("original image",oriimage)
cv2.imshow("resize image",newimage)
cv2.waitKey(0)
