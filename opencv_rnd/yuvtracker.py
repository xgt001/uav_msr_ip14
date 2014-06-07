import cv2.cv as cv
import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
# cv.NamedWindow('YUV', cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow('HSV', cv.CV_WINDOW_NORMAL)
# cv.NamedWindow('SKIN', cv.CV_WINDOW_AUTOSIZE)

cv.ResizeWindow("HSV",900,900);

# cv2.createTrackbar('Y_min','YUV',0,255,nothing)
# cv2.createTrackbar('Y_max','YUV',0,255,nothing)
# cv2.createTrackbar('Cb_min','YUV',0,255,nothing)
# cv2.createTrackbar('Cb_max','YUV',0,255,nothing)
# cv2.createTrackbar('Cr_min','YUV',0,255,nothing)
# cv2.createTrackbar('Cr_max','YUV',0,255,nothing)
# cv2.createTrackbar('H_min','HSV',0,180,nothing)
# cv2.createTrackbar('H_max','HSV',0,180,nothing)
# cv2.createTrackbar('S_min','HSV',0,255,nothing)
# cv2.createTrackbar('S_max','HSV',0,255,nothing)
# cv2.createTrackbar('V_min','HSV',0,255,nothing)
# cv2.createTrackbar('V_max','HSV',0,255,nothing)

while True:
	frame=cv2.imread('image.jpg')
	
	frame=cv2.GaussianBlur(frame,(3,3), 5)
	# y_min=cv2.getTrackbarPos('Y_min','YUV')
	# Cb_min=cv2.getTrackbarPos('Cb_min','YUV')
	# Cr_min=cv2.getTrackbarPos('Cr_min','YUV')

	# y_max=cv2.getTrackbarPos('Y_max','YUV')
	# Cb_max=cv2.getTrackbarPos('Cb_max','YUV')
	# Cr_max=cv2.getTrackbarPos('Cr_max','YUV')

	# h_min = cv2.getTrackbarPos('H_min', 'HSV');
	# s_min = cv2.getTrackbarPos('S_min', 'HSV');
	# v_min = cv2.getTrackbarPos('V_min', 'HSV');

	# h_max = cv2.getTrackbarPos('H_max', 'HSV');
	# s_max = cv2.getTrackbarPos('S_max', 'HSV');
	# v_max = cv2.getTrackbarPos('V_max', 'HSV');

	# yuv=cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# skin=cv2.inRange(yuv, (0,133,77), (255,173,127))
	# yuv_skin=cv2.inRange(yuv, (y_min,Cb_min,Cr_min), (y_max,Cb_max,Cr_max))
	# hsv_skin=cv2.inRange(hsv, (h_min,s_min,v_min), (h_max,s_max,v_max))
	hsv_skin=cv2.inRange(hsv, (10,0,0), (80,255,255))
	# yuv_skin=cv2.medianBlur(yuv_skin, 3)

	hsv_skin=cv2.medianBlur(hsv_skin, 3)
	# cv2.imshow('YUV', yuv_skin) 


	ctr = cv2.medianBlur(~hsv_skin, 1)
	contours, hierarchy = cv2.findContours(ctr,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	areas = [cv2.contourArea(c) for c in contours]
	for c in contours:
		if cv2.contourArea(c)<5000 and cv2.contourArea(c)>2000:
			cv2.drawContours(frame,c, -1,(0,0, 255),3)


	cv2.imshow( 'HSV', frame)
	# cv2.imshow('SKIN',   yuv_skin & hsv_skin )
	c = cv.WaitKey(1)
	if c == 27 : 
		break

