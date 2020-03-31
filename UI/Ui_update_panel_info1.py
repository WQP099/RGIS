# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_number.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Upadte_Number(object):
    def setupUi(self, Upadte_Number):
        Upadte_Number.setObjectName("Upadte_Number")
        Upadte_Number.resize(400, 212)
        self.label = QtWidgets.QLabel(Upadte_Number)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.new_number_value = QtWidgets.QLineEdit(Upadte_Number)
        self.new_number_value.setGeometry(QtCore.QRect(60, 70, 181, 21))
        self.new_number_value.setObjectName("new_number_value")
        self.Ok_button = QtWidgets.QPushButton(Upadte_Number)
        self.Ok_button.setGeometry(QtCore.QRect(40, 150, 93, 28))
        self.Ok_button.setObjectName("Ok_button")
        self.Cancel_button = QtWidgets.QPushButton(Upadte_Number)
        self.Cancel_button.setGeometry(QtCore.QRect(260, 150, 93, 28))
        self.Cancel_button.setObjectName("Cancel_button")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.retranslateUi(Upadte_Number)
        self.Cancel_button.clicked.connect(Upadte_Number.close)
        QtCore.QMetaObject.connectSlotsByName(Upadte_Number)

    def retranslateUi(self, Upadte_Number):
        _translate = QtCore.QCoreApplication.translate
        Upadte_Number.setWindowTitle(_translate("Upadte_Number", "重新编号"))
        self.label.setText(_translate("Upadte_Number", "请输入新的编号："))
        self.Ok_button.setText(_translate("Upadte_Number", "确定"))
        self.Cancel_button.setText(_translate("Upadte_Number", "取消"))
