import os
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ImageViewer(QtGui.QMainWindow):

    def __init__(self):
        super(ImageViewer, self).__init__()

        self.printer = QtGui.QPrinter()
        self.scaleFactor = 0.0

        self.imageLabel = QtGui.QLabel()
        self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.imageLabel.setSizePolicy(QtGui.QSizePolicy.Ignored,QtGui.QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.setCentralWidget(self.scrollArea)
        self.setCursor(Qt.CrossCursor)
        self.createActions()
        self.createMenus()
        self.setWindowTitle("Edhitha Image Processor (Dev)")
        self.resize(800, 600)
        self.x = 0

    #open folder patch
    def open(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, "Open File",
                QtCore.QDir.currentPath())
        if fileName:
            print fileName
            image = QtGui.QImage(fileName)
            if image.isNull():
                QtGui.QMessageBox.information(self, "Image Viewer",
                        "Cannot load %s." % fileName)
                return

            self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
            self.scaleFactor = 1.0
            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.updateActions()

            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()

    def openDirectory(self,e):
        global fileDirectory
        fileDirectory = QtGui.QFileDialog.getExistingDirectory(self, "Open Directory", "/home" ,QtGui.QFileDialog.ShowDirsOnly| QtGui.QFileDialog.DontResolveSymlinks);
        if fileDirectory:
          # QtGui.QMessageBox.information(self,"Image Viewer","Success")
            print fileDirectory
            global list_files
            global fcount
            fcount = 0
            list_files = os.listdir(fileDirectory)
            print list_files
        if list_files[0]:
            fileName = list_files[0]
            image = QtGui.QImage(fileDirectory+"/"+fileName)
            if image.isNull():
                QtGui.QMessageBox.information(self, "Image Viewer",
                        "Cannot load %s." % fileName)
                return
            self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
            self.scaleFactor = 1.0
            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.updateActions()

            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()

    def keyPressEvent(self, e):
        global fcount
        if e.key() == QtCore.Qt.Key_S:
            fcount = fcount + 1
            if(fcount==len(list_files)):
                fileName = list_files[0]
                fcount = 0
            else:
                fileName = list_files[fcount]
            image = QtGui.QImage(fileDirectory+"/"+fileName)
            print fileName
            if image.isNull():
                QtGui.QMessageBox.information(self, "Image Viewer","Cannot load %s." % fileName)
                return
            self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
            self.scaleFactor = 1.0
            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.updateActions()
            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()

        if e.key() == QtCore.Qt.Key_A:
            fcount = fcount-1
            if(fcount==-1):
                fileName = list_files[len(list_files)-1]
                fcount = len(list_files)-1
            else:
                fileName = list_files[fcount]
            image = QtGui.QImage(fileDirectory+"/"+fileName)
            print fileName
            if image.isNull():
                QtGui.QMessageBox.information(self, "Image Viewer","Cannot load %s." % fileName)
                return
            self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
            self.scaleFactor = 1.0
            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.updateActions()
            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()

    def print_(self):
        dialog = QtGui.QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QtGui.QPainter(self.printer)
            rect = painter.viewport()
            size = self.imageLabel.pixmap().size()
            size.scale(rect.size(), QtCore.Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabel.pixmap().rect())
            painter.drawPixmap(0, 0, self.imageLabel.pixmap())


    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def wheelEvent(self, event):
        # wheelie event attribute has a delta method
        # this returns positive when zoomIn and negative when zoomout
        print "Working wheelie"
        k = event.delta()
        if k > 0:
            self.zoomIn()
        else:
            self.zoomOut()

    def normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0


    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()

        self.updateActions()

    def mouseMoveEvent (self, event):
        self.x = event.pos().x()
        self.y = event.pos().y()
        self.update()
        print self.x

  
    #change
    def about(self):
        QtGui.QMessageBox.about(self, "Editha 2014","Pre Alpha")

    def createActions(self):
        self.openAct = QtGui.QAction("&Open...", self, shortcut="Ctrl+O",triggered=self.open)

        self.printAct = QtGui.QAction("&Print...", self, shortcut="Ctrl+P",enabled=False, triggered=self.print_)

        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",triggered=self.close)

        self.openDirectoryAct =  QtGui.QAction("&OpenFolder...", self, shortcut="Ctrl+F",triggered=self.openDirectory)

        self.zoomInAct = QtGui.QAction("Zoom &In (25%)", self,shortcut="Ctrl++", enabled=False, triggered=self.zoomIn)

        self.zoomOutAct = QtGui.QAction("Zoom &Out (25%)", self,shortcut="Ctrl+-", enabled=False, triggered=self.zoomOut)

        self.normalSizeAct = QtGui.QAction("&Normal Size", self, shortcut="Ctrl+S", enabled=False, triggered=self.normalSize)

        self.fitToWindowAct = QtGui.QAction("&Fit to Window", self, enabled=True, checkable=True, shortcut="Ctrl+K",triggered=self.fitToWindow)

        self.aboutAct = QtGui.QAction("&About", self, triggered=self.about)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,triggered=QtGui.qApp.aboutQt)

    def createMenus(self):
        self.fileMenu = QtGui.QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addAction(self.openDirectoryAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QtGui.QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)

        self.helpMenu = QtGui.QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.viewMenu)
        self.menuBar().addMenu(self.helpMenu)

    def updateActions(self):
        self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())


    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()+((factor - 1) * scrollBar.pageStep()/2)))



if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    imageViewer = ImageViewer()
    imageViewer.show()
    sys.exit(app.exec_())