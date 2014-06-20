# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sheet_gen_ui.ui'
#
# Created: Tue Jun 17 17:13:11 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.inp_target_shape = QtGui.QPlainTextEdit(self.centralwidget)
        self.inp_target_shape.setGeometry(QtCore.QRect(140, 370, 131, 31))
        self.inp_target_shape.setObjectName(_fromUtf8("inp_target_shape"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 420, 91, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 370, 91, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.inp_char = QtGui.QPlainTextEdit(self.centralwidget)
        self.inp_char.setGeometry(QtCore.QRect(480, 370, 131, 31))
        self.inp_char.setObjectName(_fromUtf8("inp_char"))



        self.inp_char.setPlainText(" ")
        # self.blobView = QtGui.QGraphicsView(self.centralwidget)
        # self.blobView.setGeometry(QtCore.QRect(250, 10, 431, 291))
        # self.blobView.setObjectName(_fromUtf8("blobView"))
        self.fit_char_button = QtGui.QPushButton(self.centralwidget)
        self.fit_char_button.setGeometry(QtCore.QRect(50, 100, 151, 41))
        self.fit_char_button.setObjectName(_fromUtf8("fit_char_button"))
        self.inp_target_color = QtGui.QPlainTextEdit(self.centralwidget)
        self.inp_target_color.setGeometry(QtCore.QRect(140, 420, 131, 31))
        self.inp_target_color.setObjectName(_fromUtf8("inp_target_color"))
        self.gen_sheet_button = QtGui.QPushButton(self.centralwidget)
        self.gen_sheet_button.setGeometry(QtCore.QRect(490, 510, 131, 31))
        self.gen_sheet_button.setObjectName(_fromUtf8("gen_sheet_button"))
        self.blob_next = QtGui.QPushButton(self.centralwidget)
        self.blob_next.setGeometry(QtCore.QRect(500, 310, 111, 31))
        self.blob_next.setObjectName(_fromUtf8("blob_next"))
        self.blob_prev = QtGui.QPushButton(self.centralwidget)
        self.blob_prev.setGeometry(QtCore.QRect(320, 310, 101, 31))
        self.blob_prev.setObjectName(_fromUtf8("blob_prev"))
        self.folder_button = QtGui.QPushButton(self.centralwidget)
        self.folder_button.setGeometry(QtCore.QRect(50, 40, 151, 41))
        self.folder_button.setObjectName(_fromUtf8("folder_button"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 370, 91, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 420, 121, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.inp_char_color = QtGui.QPlainTextEdit(self.centralwidget)
        self.inp_char_color.toPlainText()
        self.inp_char_color.setGeometry(QtCore.QRect(480, 420, 131, 31))
        self.inp_char_color.setObjectName(_fromUtf8("inp_char_color"))
        self.insert_entry_button = QtGui.QPushButton(self.centralwidget)
        self.insert_entry_button.setGeometry(QtCore.QRect(260, 510, 131, 31))
        self.insert_entry_button.setObjectName(_fromUtf8("insert_entry_button"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Edhitha Blob Characterizer (Dev)", None))
        self.label_3.setText(_translate("MainWindow", "Target Color", None))
        self.label_2.setText(_translate("MainWindow", "Target Shape", None))
        self.fit_char_button.setText(_translate("MainWindow", "Auto Detect", None))
        self.gen_sheet_button.setText(_translate("MainWindow", "Generate TXT", None))
        self.blob_next.setText(_translate("MainWindow", "Next", None))
        self.blob_prev.setText(_translate("MainWindow", "Previous", None))
        self.folder_button.setText(_translate("MainWindow", "Select Blob Folder", None))
        self.label_4.setText(_translate("MainWindow", "Character", None))
        self.label_5.setText(_translate("MainWindow", "Character Color", None))
        self.insert_entry_button.setText(_translate("MainWindow", "Append Entry", None))

