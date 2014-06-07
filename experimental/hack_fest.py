import os
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Point():
    color = Qt.black
    x = 0
    y = 0

    def color(self): return self.color
    def x(self): return self.x
    def y(self): return self.y

    def __init__(self, x, y, color = Qt.black):
        self.x = x
        self.y = y
        self.color = color

class Square():

    FIELD = 0
    SELECTION = 1

    point_1 = Point(0, 0)
    point_2 = Point(0, 0)
    x1, x2, y1, y2, h, w = 0, 0, 0, 0, 0, 0
    color = Qt.black
    childs = []

    def addChild(self, square):
        self.childs.append(square)

    def type(self):
        if (len(self.childs) > 0):
            return self.FIELD
        else:
            return self.SELECTION

    def __init__(self, point_1, point_2, color = Qt.black):
        self.childs = []
        self.x1 = min(point_1.x, point_2.x)
        self.y1 = min(point_1.y, point_2.y)
        self.x2 = max(point_1.x, point_2.x)
        self.y2 = max(point_1.y, point_2.y)
        self.h  = self.y2 - self.y1
        self.w  = self.x2 - self.x1
        self.color = color


class ImageDrawPanel(QGraphicsPixmapItem):
    #fieldMarkModeEnabled = False
    fieldMark = None

    def __init__(self, pixmap = None, parent = None, scene = None):
        self.p1 = None
        self.p2 = None

        super(ImageDrawPanel, self).__init__()
        self.x, self.y = -1, -1

        self.pen = self.createPen(Qt.blue)

    def createPen(self, color = Qt.black):
        pen = QPen(Qt.SolidLine)
        pen.setColor(color)
        pen.setWidth(1)
        return pen
    '''
    def togleFieldMarkMode(self):
        self.fieldMarkModeEnabled = not self.fieldMarkModeEnabled
        if self.fieldMarkModeEnabled:
            self.pen.setColor(Qt.red)
            print "Field Mark Mode [ ON  ]"
        else:
            self.pen.setColor(Qt.blue)
            print "Field Mark Mode [ OFF ]"
        self.update()
    '''
    def drawCross(self, painter, point):
        painter.setPen(self.createPen(point.color))
        painter.drawLine(point.x, point.y - 100, point.x, point.y + 100)
        painter.drawLine(point.x - 100, point.y, point.x + 100, point.y)

    def drawSquare(self, painter, square):
        painter.setPen(self.createPen(square.color))
        painter.drawRect(square.x1, square.y1, square.w, square.h)

    '''
    def markPoint(self, x, y):
        if self.p1 == None:
            self.p1 = Point(x, y, self.pen.color())
        else:
            self.p2 = Point(x, y, self.pen.color())
    '''
    def cleanTempMarks(self):
        self.x = -1
        self.y = -1
        self.p1 = None
        self.p2 = None

    def cleanAll(self):
        if self.fieldMark != None:
            self.fieldMark.childs = None
        self.fieldMark = None
        self.cleanTempMarks()

    def paint(self, painter, option, widget = None):
        painter.drawPixmap(0, 0, self.pixmap())
        #painter.setPen(self.pen)


        if self.fieldMark != None:
            self.drawSquare(painter, self.fieldMark)
            for child in self.fieldMark.childs:
                self.drawSquare(painter, child)


        ''' DRAW TIME
        '''
        if self.p1 != None:
            self.drawCross(painter, self.p1)

        if self.p2 != None:
            ''' THIS IS NOT GOOD!
            '''
            point_1 = Point(self.p1.x, self.p1.y, self.pen.color())
            point_2 = Point(self.p2.x, self.p2.y, self.pen.color())
            square = Square(point_2, point_1, self.pen.color())

            if self.fieldMark == None:
                self.fieldMark = square
            else:
                self.fieldMark.addChild(square)


            ''' LIMPAR
            '''
            self.cleanTempMarks()
            ''' LIMPAR
            '''

            self.update()

            #self.drawCross(painter, self.p2)
        else:
            if self.x >= 0 and self.y >= 0:
                ponto_2 = Point(self.x, self.y, self.pen.color())
                self.drawSquare(painter, Square(self.p1, ponto_2, self.pen.color()))

        '''DRAW TIME
        '''
        #if self.fieldMark != None:
        #    self.drawSquare(painter, self.fieldMark)
        #    self.p1 = None
        #    self.p2 = None

    #def update(self, *args, **kwargs):
    #    if (self.fieldMarkModeEnabled):
    #        self.fieldMark = Square(self.p1, self.p2, self.pen.color())
    #    return QGraphicsPixmapItem.update(self, *args, **kwargs)

    def mousePressEvent (self, event):
        x = event.pos().x()
        y = event.pos().y()
        self.p1 = Point(x, y, self.pen.color())
        self.update()

    def mouseReleaseEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        self.p2 = Point(x, y, self.pen.color())
        self.update()

    def mouseMoveEvent (self, event):
        self.x = event.pos().x()
        self.y = event.pos().y()
        self.update()


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

        self.scene = QGraphicsScene()
        #The QGraphicsScene class provides a surface for managing a large number of 2D graphical items.
        #The class serves as a container for QGraphicsItems
        self.scene.setSceneRect(0,0,800,600)
        # set scene size
        #self.pixmaps = self.getImages()
        self.imagepanel = ImageDrawPanel(scene=self.scene)
        self.scene.addItem(self.imagepanel) #add item to the scene graphics container, an image panel..


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
            self.imagepanel.cleanAll()
            self.imagepanel.setPixmap(QtGui.QPixmap.fromImage(image))
            self.imagepanel.update()
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