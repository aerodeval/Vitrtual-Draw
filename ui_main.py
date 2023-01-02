# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainlBleoO.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import cv2
import os
from PIL import Image
import easygui
import subprocess
path=" "


class Ui_MainWindow(object):


    def execute(self):
        im = Image.open("C:/Users/wgome/Desktop/VirtualDraw/spider.png")
        im.show()
        easygui.msgbox("we recommend you to use your numpad key as it is easier to navigate for changing color hence please press numlock", title="important!!!")
        os.system('python final.py')




    #def patret(self):
        #return self.open_dialog_box().path

    def getPath(self):
        return self.path

    def open_dialog_box(self):
        global path
        im = Image.open("C:/Users/wgome/Desktop/VirtualDraw/spider.png")
        im.show()
        easygui.msgbox(
            "we recommend you to use your numpad key as it is easier to navigate for changing color hence please press numlock",
            title="important!!!")
        filename = QFileDialog.getOpenFileName()
        path1 = filename[0]
        print(path1)
        self.path=path1
        #os.system(f'python recent.py "{path1}"')
        subprocess.call(['python', 'recent.py', path1])



    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(774, 552)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color:rgb(56, 58, 89);\n"
"QFrame {		\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(self.open_dialog_box)
        self.pushButton_2.setMaximumSize(QSize(767, 16777215))
        font1 = QFont()
        font1.setPointSize(26)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"color: rgb(238, 210, 255)")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.execute)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"color: rgb(238, 210, 255);\n"
"border-color: rgb(197, 250, 255);\n"
"")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Start drawing on a recent image", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Press the button to start drawing", None))
    # retranslateUi
    print(path)