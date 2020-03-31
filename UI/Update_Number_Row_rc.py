# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Update_Number_Row.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Update_number_Dialog(object):
    def setupUi(self, Update_number_Dialog):
        Update_number_Dialog.setObjectName("Update_number_Dialog")
        Update_number_Dialog.resize(400, 212)
        self.label = QtWidgets.QLabel(Update_number_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 180, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Number_value = QtWidgets.QLineEdit(Update_number_Dialog)
        self.Number_value.setGeometry(QtCore.QRect(70, 70, 181, 30))
        self.Number_value.setObjectName("Number_value")
        self.Ok_button = QtWidgets.QPushButton(Update_number_Dialog)
        self.Ok_button.setGeometry(QtCore.QRect(40, 170, 93, 28))
        self.Ok_button.setObjectName("Ok_button")
        self.Cancel_button = QtWidgets.QPushButton(Update_number_Dialog)
        self.Cancel_button.setGeometry(QtCore.QRect(260, 170, 93, 28))
        self.Cancel_button.setObjectName("Cancel_button")
        self.label_2 = QtWidgets.QLabel(Update_number_Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 321, 16))
        self.label_2.setObjectName("label_2")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.retranslateUi(Update_number_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Update_number_Dialog)

    def retranslateUi(self, Update_number_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Update_number_Dialog.setWindowTitle(_translate("Update_number_Dialog", "Dialog"))
        self.label.setText(_translate("Update_number_Dialog", "请输入单行编号格式："))
        self.Number_value.setPlaceholderText(_translate("Update_number_Dialog", "0,1,x"))
        self.label_2.setText(_translate("Update_number_Dialog", "0为行,1为列,x为单个编号"))
        self.Ok_button.setText(_translate("Update_number_Dialog", "确定"))
        self.Cancel_button.setText(_translate("Update_number_Dialog", "取消"))
