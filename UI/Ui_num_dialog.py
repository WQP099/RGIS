# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'num_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator


class Ui_numDialog(object):
    def setupUi(self, numDialog):
        numDialog.setObjectName("numDialog")
        numDialog.resize(400, 212)
        self.label = QtWidgets.QLabel(numDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 153, 33))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Num_value = QtWidgets.QLineEdit(numDialog)
        self.Num_value.setGeometry(QtCore.QRect(70, 60, 181, 20))
        self.Num_value.setObjectName("Num_value")
        self.Num_value.setPlaceholderText("请输入整数")
        self.Num_value.setValidator(QtGui.QIntValidator())
        pIntvalidator = QIntValidator(self)
        pIntvalidator.setRange(1,99)
        self.Num_value.setValidator(pIntvalidator)


        self.Ok_button = QtWidgets.QPushButton(numDialog)
        self.Ok_button.setGeometry(QtCore.QRect(40, 170, 93, 28))
        self.Ok_button.setObjectName("Ok_button")
        self.Cancel_button = QtWidgets.QPushButton(numDialog)
        self.Cancel_button.setGeometry(QtCore.QRect(260, 170, 93, 28))
        self.Cancel_button.setObjectName("Cancel_button")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.retranslateUi(numDialog)

        QtCore.QMetaObject.connectSlotsByName(numDialog)

    def retranslateUi(self, numDialog):
        _translate = QtCore.QCoreApplication.translate
        numDialog.setWindowTitle(_translate("numDialog", "Dialog"))
        self.label.setText(_translate("numDialog", "请输入整行数量："))
        self.Ok_button.setText(_translate("numDialog", "保存"))
        self.Cancel_button.setText(_translate("numDialog", "取消"))
