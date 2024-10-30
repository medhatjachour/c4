# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileNamekOSYzt.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)
class Ui_Form(QFrame):
    def __init__(
        self,
        text,
    ):
        super().__init__()
        self._text = text
        self.resize(811, 80)
        self.setStyleSheet(u"background-color: rgb(46, 46, 46);\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 3, 3)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.delete_2 = QPushButton(self.frame)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setMinimumSize(QSize(50, 50))
        self.delete_2.setMaximumSize(QSize(50, 50))
        self.delete_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_2.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"\n"
"/*border:2px solid rgb(222, 0, 0);*/\n"
"font-family: Proxima Nova;\n"
"font-size: 16px;\n"
"font-weight: 700;\n"
"line-height: 16px;\n"
"text-align: center;\n"
"color : white;\n"
"border-radius: 25px;\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"../icons/trash2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_2.setIcon(icon)
        self.delete_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.delete_2)


        self.horizontalLayout.addWidget(self.frame)
        self.delete_2.clicked.connect(self.deleteFun)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi
    def deleteFun(self):
        self.hide()
    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(self._text)
        self.delete_2.setText("")
    # retranslateUi

