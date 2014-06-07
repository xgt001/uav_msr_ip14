#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
author: Ganesh Hegde
last edited: June 2014
"""

import sys
import os
import cv2
from PyQt4 import QtGui, QtCore


class AutoProcessCore(QtGui.QMainWindow):

    def __init__(self):
        super(AutoProcessCore, self).__init__()

        self.initUI()

    def initUI(self):

        btn1 = QtGui.QPushButton("Source", self)

        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Blob", self)
        btn2.move(150, 50)

        btn3 = QtGui.QPushButton("Begin",self)
        btn3.move(30,100)

        self.sourceLocation = " "
        self.blobLocation = " "

        btn1.clicked.connect(self.setLocationPicker)
        btn2.clicked.connect(self.setLocationPicker)
        btn3.clicked.connect(self.autoProcess)

        self.statusBar()
        self.setGeometry(300, 300, 800, 600)

        self.setWindowTitle('Edhitha Auto Image Processor (Dev)')
        self.show()
    #
    # def buttonClicked(self):
    #
    #     sender = self.sender()
    #     self.statusBar().showMessage(sender.text() + ' was pressed')
    #     print sender.text()

    def setLocationPicker(self):
        global fileDirectory
        fileDirectory = QtGui.QFileDialog.getExistingDirectory(self, "Open Directory", "/home/ganesh/edhitha/" ,QtGui.QFileDialog.ShowDirsOnly| QtGui.QFileDialog.DontResolveSymlinks);
        if fileDirectory:
          # QtGui.QMessageBox.information(self,"Image Viewer","Success")
          #   print fileDirectory
            global list_source_images
            global list_blob_images
            fcount = 0

            sender = self.sender()
            if sender.text() == "Blob":
                self.blobLocation = fileDirectory
                #DEBUG flags
                print self.blobLocation
                print self.sourceLocation
                print 'Blob was clicked'
            elif sender.text() == "Source":
                self.sourceLocation = fileDirectory
                list_source_images = os.listdir(fileDirectory)

                #
                # #DEBUG flags
                print 'Source was clicked'
                # print self.blobLocation
                # print self.sourceLocation

    def autoProcess(self):
        print "Inside OpenCV module Core"
        if len(self.blobLocation)== 1 | len(self.blobLocation) == 1 :
            print "showing Location NOT set dialog"
            QtGui.QMessageBox.about(self, "Alert", "Blob Location or Source Location weren't set")


        #     print list_files
        # if list_files[0]:
        #     fileName = list_files[0]
        #     image = QtGui.QImage(fileDirectory+"/"+fileName)
        #     if image.isNull():
        #         QtGui.QMessageBox.information(self, "Image Viewer",
        #                 "Cannot load %s." % fileName)
        #         return
        #     self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
        #     self.scaleFactor = 1.0
        #     self.printAct.setEnabled(True)
        #     self.fitToWindowAct.setEnabled(True)
        #     self.updateActions()
        #
        #     if not self.fitToWindowAct.isChecked():
        #         self.imageLabel.adjustSize()

        #TODO we Ignore the image populate code for now, needs to be taken care of for the populator


        print list_source_images

        for file in list_source_images:

            filename = self.sourceLocation+'/'+file

            # QtCore.
            print filename
            image = cv2.imread(str(filename))
            newx,newy = image.shape[1]/6,image.shape[0]/6 #new size (w,h)
            img = cv2.resize(image,(newx,newy))

            img_sav = img
            # CODE: Resize Image Toggle
            # cv2.imshow("resize image",img)
            # cv2.waitKey(0)


            img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

            retval, threshold = cv2.threshold(img,170,200,cv2.THRESH_BINARY_INV)
            #
            # cv2.imshow("threshold",threshold)
            # cv2.waitKey(0)

            # contours,hierarchy = cv2.findContours(threshold,1,2)

            contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            contours.sort(key=cv2.contourArea, reverse=True)

            #DOCUMENTATION
            #


            for i in range(0,100,1):

                ret = cv2.matchShapes(contours[i],contours[i+1],1,0.0)
                if cv2.contourArea(contours[i]) < 300 and cv2.contourArea(contours[i]) > 50 and ret < 5 and ret > 0 :

                    print "match:"; print ret
                    print "Area:"; print cv2.contourArea(contours[i])
                    cv2.drawContours(img_sav,contours,i,(0,255,0),1)
                    x,y,w,h = cv2.boundingRect(contours[i])
                    cv2.rectangle(img_sav,(x,y),(x+w,y+h),(0,255,0),2)
                    # cv2.imshow("test",img_sav) #disable showing the images while processing
                    cv2.imwrite(str(self.blobLocation)+"blob"+str(i)+'.png', img_sav[y:y+h,x:x+w])
                    # cv2.waitKey(0)

            # for cnt_detect in contours:
            #     area = cv2.contourArea(cnt_detect)
            #     if area > 2000:
            #         # (x,y),radius = cv2.minEnclosingCircle(cnt_detect)
            #         # center = (int(x),int(y))
            #         # radius = int(radius)
            #         # threshold = cv2.circle(threshold,center,radius,(0,255,0),2)
            #         # cv2.drawContours(threshold,cnt_detect,)
            #         print area
            #         cv2.drawContours(img_sav,cnt_detect, 0, (0,255,0), 7)
            #         cv2.imshow("test",img_sav)
            #         cv2.waitKey(0)
            # # contour filtering



            #draw all contours
            # cv2.drawContours(img_sav, contours, -1, (0,255,0), 3)


            # cv2.drawContours(img_sav, contours, 7, (255, 0, 0), 2)

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


            # cv2.imshow("contour extract",img_sav)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = AutoProcessCore()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
