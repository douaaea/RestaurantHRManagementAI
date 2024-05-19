# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\faceRecognition.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FaceRecognition(object):
    def setupUi(self, FaceRecognition):
        FaceRecognition.setObjectName("FaceRecognition")
        FaceRecognition.resize(1009, 638)
        self.widget = QtWidgets.QWidget(FaceRecognition)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1011, 641))
        self.widget.setStyleSheet("#widget{\n"
"background-color:#677B5E;\n"
"}")
        self.widget.setObjectName("widget")
        self.cameraWidget = QtWidgets.QWidget(self.widget)
        self.cameraWidget.setGeometry(QtCore.QRect(10, 10, 671, 531))
        self.cameraWidget.setObjectName("cameraWidget")
        self.clockinButton = QtWidgets.QPushButton(self.widget)
        self.clockinButton.setGeometry(QtCore.QRect(40, 560, 291, 61))
        self.clockinButton.setStyleSheet("#clockinButton{\n"
"background-color:#B8CBB0;\n"
"}\n"
"#clockinButton:hover{\n"
"background-color:#BC9C22;\n"
"}")
        self.clockinButton.setObjectName("clockinButton")
        self.clockoutButton = QtWidgets.QPushButton(self.widget)
        self.clockoutButton.setGeometry(QtCore.QRect(370, 560, 291, 61))
        self.clockoutButton.setStyleSheet("#clockoutButton{\n"
"background-color:#B8CBB0;\n"
"}\n"
"#clockoutButton:hover{\n"
"background-color:#BC9C22;\n"
"}")
        self.clockoutButton.setObjectName("clockoutButton")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(700, 30, 301, 581))
        self.widget_2.setStyleSheet("#widget_2{\n"
"background-color:#B8CBB0;\n"
"}\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.groupBox = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 120, 271, 271))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 30, 139, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(120, 30, 131, 211))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.NameLabel_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.NameLabel_2.setFont(font)
        self.NameLabel_2.setText("")
        self.NameLabel_2.setObjectName("NameLabel_2")
        self.verticalLayout_4.addWidget(self.NameLabel_2)
        self.StatusLabel_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.StatusLabel_2.setFont(font)
        self.StatusLabel_2.setText("")
        self.StatusLabel_2.setObjectName("StatusLabel_2")
        self.verticalLayout_4.addWidget(self.StatusLabel_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.HoursLabel_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.HoursLabel_2.setFont(font)
        self.HoursLabel_2.setText("")
        self.HoursLabel_2.setObjectName("HoursLabel_2")
        self.horizontalLayout_3.addWidget(self.HoursLabel_2)
        self.MinLabel_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MinLabel_2.setFont(font)
        self.MinLabel_2.setText("")
        self.MinLabel_2.setObjectName("MinLabel_2")
        self.horizontalLayout_3.addWidget(self.MinLabel_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 281, 72))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.Date_Label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Date_Label_2.setFont(font)
        self.Date_Label_2.setObjectName("Date_Label_2")
        self.gridLayout_3.addWidget(self.Date_Label_2, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.Time_Label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Time_Label_2.setFont(font)
        self.Time_Label_2.setObjectName("Time_Label_2")
        self.gridLayout_3.addWidget(self.Time_Label_2, 1, 1, 1, 1)

        self.retranslateUi(FaceRecognition)
        QtCore.QMetaObject.connectSlotsByName(FaceRecognition)

    def retranslateUi(self, FaceRecognition):
        _translate = QtCore.QCoreApplication.translate
        FaceRecognition.setWindowTitle(_translate("FaceRecognition", "Form"))
        self.clockinButton.setText(_translate("FaceRecognition", "CLOCK IN"))
        self.clockoutButton.setText(_translate("FaceRecognition", "CLOCK OUT"))
        self.groupBox.setTitle(_translate("FaceRecognition", "Details"))
        self.label_6.setText(_translate("FaceRecognition", "Name : "))
        self.label_7.setText(_translate("FaceRecognition", "Status :"))
        self.label_8.setText(_translate("FaceRecognition", "Clocked Time : "))
        self.label_9.setText(_translate("FaceRecognition", "Date :"))
        self.Date_Label_2.setText(_translate("FaceRecognition", "-"))
        self.label_10.setText(_translate("FaceRecognition", "Time :"))
        self.Time_Label_2.setText(_translate("FaceRecognition", "-"))
