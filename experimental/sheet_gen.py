__author__ = 'ganesh'

import sys
from PyQt4 import QtCore, QtGui, uic
import os
import exifread

form_class = uic.loadUiType("sheet_gen_ui.ui")[0]                 # Load the UI

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # self.read_exif_data(self)
        # self.blobView.
        # self.blobView = QtGui
        # self.blobView = QtGui.QGraphicsView(self.centralwidget)


        self.scn = QtGui.QGraphicsScene()
        self.pic = QtGui.QLabel(self.centralwidget)
        self.pic.setGeometry(QtCore.QRect(250, 10, 431, 291))

        self.folder_button.clicked.connect(self.load_images)
        self.insert_entry_button.clicked.connect(self.file_writer)
        self.blob_prev.clicked.connect(self.prev_image)
        self.blob_next.clicked.connect(self.next_image)
        global temp
        temp = 0


    #     self.btn_CtoF.clicked.connect(self.btn_CtoF_clicked)  # Bind the event handlers
    #     self.btn_FtoC.clicked.connect(self.btn_FtoC_clicked)  #   to the buttons
    #
    # def btn_CtoF_clicked(self):                  # CtoF button event handler
    #     cel = float(self.editCel.text())         #
    #     fahr = cel * 9 / 5.0 + 32                #
    #     self.spinFahr.setValue(int(fahr + 0.5))  #
    #
    # def btn_FtoC_clicked(self):                  # FtoC button event handler
    #     fahr = self.spinFahr.value()             #
    #     cel = (fahr - 32) *                      #
    #     self.editCel.setText(str(cel))           #


    def read_exif_data(self,file):
        if not file:
            print "file data not yet loaded"
        self.read_file_exif = open(file,"rb")

        global tags
        tags = exifread.process_file(self.read_file_exif)

        print "Inside EXIF reading function"
        # for tag in tags.keys():
        #     # if self.tag in ('GPS GPSLatitude', 'GPS GPSLongitude','GPS GPSAltitude','Image Orientation'):
        #     #     print "Key: %s, value %s" % (self.tag, self.tags[self.tag])
        #     print "Key: %s, value %s" % (tag, tags[tag])


    def file_writer(self):
        #
        for tag in tags.keys():
            if tag in ('GPS GPSLatitude', 'GPS GPSLongitude','GPS GPSAltitude'):
                value2 =   tags['GPS GPSLatitude']
                value3 =   tags['GPS GPSLongitude']

        value_targetColor = self.inp_target_shape.toPlainText()

        value_targetShape = self.inp_target_color.toPlainText()

        value_char = self.inp_char.toPlainText()

        value_charColor = self.inp_char_color.toPlainText()

        print value_char, value_targetColor, value_targetShape, value_charColor

        print "Writing Params"

        sheetTitle = "MSRIT.txt"

        fileCheck = os.path.isfile(sheetTitle)

        value1 = fcount


        value5 = value_targetShape

        value6 = value_targetColor

        value7 = value_char

        value8 = value_charColor

        temp = fcount
        if not fileCheck:
            print "Creating new file"
            data_sheet = open("MSRIT.txt","a")
            print "Temp is ",temp
            if temp == 0:
                data_sheet.write("0 \t 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \n")
                data_sheet.write("____________________________________________________________________________ \n")
                data_sheet.write(str(value1)+" \t"+str(value2)+" \t"+str(value3)+" \t ")
                data_sheet.write(str(value5)+" \t"+str(value6)+" \t"+str(value7)+"\t"+str(value8)+"\t \n")
            if temp > 0:
                data_sheet.write(str(value1)+" \t"+str(value2)+" \t"+str(value3)+" \t ")
                data_sheet.write(str(value5)+" \t"+str(value6)+" \t"+str(value7)+"\t"+str(value8)+"\t \n")
            data_sheet.close()
        else:
            print "File already exists"
            data_sheet = open("MSRIT.txt","a")
            print "Temp is ",temp
            if temp> 0:
                data_sheet.write(str(value1)+" \t"+str(value2)+" \t"+str(value3)+" \t ")
                data_sheet.write(str(value5)+" \t"+str(value6)+" \t"+str(value7)+"\t"+str(value8)+"\t \n")
            data_sheet.close()


        # data_sheet.write(""+blob_id+"\t")

        print "Inside EXIF reading function"



        # print type(value2), type(value3)


        print "Written Parameters"


    def clear_text_fields(self):

        self.inp_target_shape.setPlainText(" ")

        self.inp_char.setPlainText(" ")

        self.inp_target_color.setPlainText(" ")

        self.inp_char.setPlainText(" ")

        self.inp_char_color.setPlainText(" ")



    def load_images(self):
        print "Loading Blobs"
        global fileDirectory
        fileDirectory = QtGui.QFileDialog.getExistingDirectory(self, "Open Directory", "/home/ganesh/edhitha/blob_extracts/" ,QtGui.QFileDialog.ShowDirsOnly| QtGui.QFileDialog.DontResolveSymlinks);
        global fcount
        if fileDirectory:
          # QtGui.QMessageBox.information(self,"Image Viewer","Success")
            print fileDirectory
            global list_files
            fcount = 0
            list_files = os.listdir(fileDirectory)
            print list_files
        if list_files[0]:
            fileName = list_files[0]
            pixmap = QtGui.QPixmap(fileDirectory+"/"+fileName)

            # read EXIF data
            file_path = fileDirectory + "/" + fileName
            self.read_exif_data(file_path)

            pixmap = pixmap.scaledToHeight(200)
            self.pic.setPixmap(pixmap)

            if pixmap:
                print "loaded image"

            # if image.isNull():
            #     QtGui.QMessageBox.information(self, "Image Viewer","Cannot load %s." % fileName)
            #     return
            # load the first image here
        self.clear_text_fields()


    def prev_image(self):
        self.file_writer()
        print "Previous Image"
        global fcount
        print fcount
        fcount = fcount - 1

        if(fcount==-1):
            fileName = list_files[len(list_files)-1]
            fcount = len(list_files)-1
        else:
           fileName = list_files[fcount]


        # read EXIF data
        file_path = fileDirectory + "/" + fileName
        self.read_exif_data(file_path)

        pixmap = QtGui.QPixmap(fileDirectory+"/"+fileName)

        pixmap = pixmap.scaledToHeight(200)
        self.pic.setPixmap(pixmap)
        if pixmap:
           print "loaded previous image"
        self.clear_text_fields()


    def next_image(self):
        self.file_writer()
        print "Next Image"
        global fcount
        print fcount
        fcount = fcount + 1
        if (fcount==len(list_files)):
           fileName = list_files[0]
           fcount = 0
        else :
            fileName = list_files[fcount]

        # read EXIF data
        file_path = fileDirectory + "/" + fileName
        self.read_exif_data(file_path)


        pixmap = QtGui.QPixmap(fileDirectory+"/"+fileName)
        pixmap = pixmap.scaledToHeight(200)
        self.pic.setPixmap(pixmap)
        if pixmap:
            print "loaded next image"
        self.clear_text_fields()


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
