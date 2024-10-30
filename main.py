# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledYmCzcU.ui'
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
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(883, 722)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"                background-color: #2e2e2e;\n"
"                color: #ffffff;		")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 152))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 40, -1, 40)
        self.browse_file = QPushButton(self.frame)
        self.browse_file.setObjectName(u"browse_file")
        self.browse_file.setMinimumSize(QSize(70, 70))
        self.browse_file.setMaximumSize(QSize(70, 70))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(35)
        font.setBold(True)
        self.browse_file.setFont(font)
        self.browse_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.browse_file.setStyleSheet(u"\n"
"text-align: center;\n"
"border:2px solid #fff ;\n"
"color : white;\n"
"border-radius: 35px;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.browse_file)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.frame_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(181, 196, 232);\n"
"	width: 14px;	\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius:0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(145, 145, 145);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-bottom"
                        "-left-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page:vertical{\n"
"	border:none\n"
"}\n"
"")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 861, 234))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 0, 0, 0)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.scrollArea_3)


        self.verticalLayout.addWidget(self.frame_3)

        self.error = QLabel(self.centralwidget)
        self.error.setObjectName(u"error")
        self.error.setStyleSheet(u"color: rgb(166, 0, 0);")
        self.error.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.error)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 61))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.scrape = QPushButton(self.frame_2)
        self.scrape.setObjectName(u"scrape")
        self.scrape.setMinimumSize(QSize(110, 30))
        self.scrape.setMaximumSize(QSize(110, 16777215))
        self.scrape.setCursor(QCursor(Qt.PointingHandCursor))
        self.scrape.setStyleSheet(u"\n"
"font-family: Proxima Nova;\n"
"font-size: 12px;\n"
"font-weight: 600;\n"
"line-height: 16px;\n"
"text-align: center;\n"
"background:rgb(25, 209, 11);\n"
"color : white;\n"
"border-radius: 12px;\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.scrape)

        self.horizontalSpacer_2 = QSpacerItem(304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.scrollArea_2 = QScrollArea(self.centralwidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(181, 196, 232);\n"
"	width: 14px;	\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius:0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(145, 145, 145);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-bottom"
                        "-left-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page:vertical{\n"
"	border:none\n"
"}\n"
"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 863, 235))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 0, 0, 0)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.browse_file.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.error.setText("")
        self.scrape.setText(QCoreApplication.translate("MainWindow", u"Scrape", None))
    # retranslateUi

