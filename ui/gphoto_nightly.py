import sys, os
# from PyQt4.QtGui import pyqtSlot
from PyQt4 import QtGui, QtCore
import paramiko
import subprocess
import os


class Gphoto(QtGui.QWidget):
    
    def __init__(self):
        super(Gphoto, self).__init__()
        #Super lets you avoid referring to the base class explicitly
        #QtGui.QWidget.__init__(self)
        self.initUI()

        
    def initUI(self):


        # gphoto capture button
        capBtn = QtGui.QPushButton('Capture Image..',self)
        capBtn.clicked.connect(self.captureSimple)
        capBtn.resize(capBtn.sizeHint())
        capBtn.move(40,40)



        timedCapture = QtGui.QPushButton('Timed Capture..',self)
        timedCapture.setGeometry(QtCore.QRect(100, 110, 121, 41))
        timedCapture.clicked.connect(self.captureTimed)
        timedCapture.resize(capBtn.sizeHint())



        self.imageQuant = QtGui.QTextEdit(self)
        self.imageQuant.setGeometry(QtCore.QRect(270, 110, 161, 31))
        # self.imageQuant.setObjectName(_fromUtf8("imageQuant"))

        self.imageTime = QtGui.QTextEdit(self)
        self.imageTime.setGeometry(QtCore.QRect(480, 110, 191, 31))

        # Qt widgets have a number of signals built in.
        # For example, when a QPushButton is clicked, it emits its clicked signal.
        # The clicked signal can be connected to a function that acts as a slot


        groupBox = QtGui.QGroupBox(self)
        groupBox.setGeometry(QtCore.QRect(90, 230, 561, 181))
        # groupBox.setTitle(groupBox,"Testing")
        groupBox.setTitle("Configure Paramaters")
        # self.groupBox.setTitle(self,"Set Parameters")



        iso_Qlist = QtCore.QStringList()

        iso_list = ["100","200","300","400","800"]

        for v in iso_list:
            iso_Qlist.append(QtCore.QString(v))

        shutter_Qlist = QtCore.QStringList()


        shutter_speed_list = [ "4000","3200","2500","2000","1600","1000"]

        for x in shutter_speed_list:
            shutter_Qlist.append(QtCore.QString(x))


        self.isoCombo = QtGui.QComboBox(groupBox)
        self.isoCombo.setGeometry(QtCore.QRect(160, 40, 101, 31))
        self.isoCombo.addItems(iso_Qlist)
        self.isoCombo.activated[str].connect(self.isoOnActivated)
        #do note the [str] parameter that is being passed here.
        # this is slightly different than the actual flow suggested in pycharm

        apperture_Qlist = QtCore.QStringList()

        apperture_list = ["1.8","2","2.2","2.5","2.8","3.2","3.5","4","4.5","5","5.6"]

        for y in apperture_list:
            apperture_Qlist.append(QtCore.QString(y))

        self.isoLabel = QtGui.QLabel(groupBox)
        self.isoLabel.setGeometry(QtCore.QRect(20, 40, 131, 41))
        self.isoLabel.setText("ISO")

        self.appertureCombo = QtGui.QComboBox(groupBox)
        self.appertureCombo.setGeometry(QtCore.QRect(430, 40, 91, 31))
        self.appertureCombo.addItems(apperture_Qlist)
        self.appertureCombo.activated[str].connect(self.apertureOnActivated)

        # self.appertureCombo.

        self.appertureLabel = QtGui.QLabel(groupBox)
        self.appertureLabel.setGeometry(QtCore.QRect(300, 30, 131, 41))
        self.appertureLabel.setText("Aperture")

        self.shutterLabel = QtGui.QLabel(groupBox)
        self.shutterLabel.setGeometry(QtCore.QRect(20, 90, 151, 41))
        self.shutterLabel.setText("Shutter Speed")

        self.shutterCombo = QtGui.QComboBox(groupBox)
        self.shutterCombo.setGeometry(QtCore.QRect(160, 100, 101, 31))
        self.shutterCombo.addItems(shutter_Qlist)

        self.shutterCombo.activated[str].connect(self.shutterActivated)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Gphoto Controller')
        #self.setWindowIcon(QtGui.QIcon('web.png'))        
        self.show()

    def captureSimple(self):
        print ('launching process')
        proc = subprocess.Popen("gphoto2 --capture-image-and-download",shell=True)

    def captureTimed(self):
        print ('checking parameters')
        I = self.imageTime.toPlainText()
        print "Image number:" + self.imageQuant.toPlainText()
        time = str(self.imageTime.toPlainText()).strip()
        quant = str(self.imageQuant.toPlainText()).strip()
        command = "gphoto2 --capture-image-and-download -I="+time+" "+"-F="+quant+" "
        print command
        timedProc = subprocess.Popen(command,shell=True)

    def isoOnActivated(self,text):
        print text

        if text == 100:
            isoProc = subprocess.Popen("gphoto2 --set-config iso=0",shell=True)
        elif text == 200:
            isoProc = subprocess.Popen("gphoto2 --set-config iso=1",shell=True)
        elif text == 400:
            isoProc = subprocess.Popen("gphoto2 --set-config iso=2",shell=True)
        else :
            isoProc = subprocess.Popen("gphoto2 --set-config iso=3",shell=True)

    def apertureOnActivated(self,text):
        print text

        if text == 1.8:
            appertureProc = subprocess.Popen("gphoto2 --set-config f-number=0",shell=True)
        elif text == 2:
            appertureProc = subprocess.Popen("gphoto2 --set-config f-number=1",shell=True)
        elif text == 2.2:
            appertureProc = subprocess.Popen("gphoto2 --set-config f-number=2",shell=True)
        elif text == 2.5:
            appertureProc = subprocess.Popen("gphoto2 --set-config f-number=3",shell=True)
        elif text == 2.8:
            appertureProc = subprocess.Popen("gphoto2 --set-config f-number=4",shell=True)
        elif text == 3.2:
            appertureProc = subprocess.Popen("gphoto2 --set-config f-number=5",shell=True)
        elif text == 3.5:
            appertureProc = subprocess.Popen("gphoto2 --set-config f-number=6",shell=True)
        elif text == 4:
            appertureProc = subprocess.Popen("gphoto2 --set-config f-number=7",shell=True)
        elif text == 4.5:
            appertureProc = subprocess.Popen("gphoto2 --set-config f-number=8",shell=True)
        elif text == 5:
            appertureProc = subprocess.Popen("gphoto2 --set-config f-number=9",shell=True)
        else :
            appertureProc = subprocess.Popen("gphoto2 --set-config f-number=10",shell=True)

    def shutterActivated(self,text):
        print text

        if text == 4000:
            shutterProc = subprocess.Popen("gphoto2 --set-config shutterspeed=0",shell=True)

        elif text == 3200:
            shutterProc = subprocess.Popen("gphoto2 --set-config shutterspeed=1",shell=True)
        elif text == 2500:
            shutterProc = subprocess.Popen("gphoto2 --set-config shutterspeed=2",shell=True)

        elif text == 2000:
            shutterProc = subprocess.Popen("gphoto2 --set-config shutterspeed=3",shell=True)
        elif text == 1600:
            shutterProc = subprocess.Popen("gphoto2 --set-config shutterspeed=4",shell=True)
        else:
            shutterProc = subprocess.Popen("gphoto2 --set-config shutterspeed=5",shell=True)

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Gphoto()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
