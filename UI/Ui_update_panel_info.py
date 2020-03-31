# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_number.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Upadte_Panel_info(object):
    def setupUi(self, Upadte_Panel_info):
        Upadte_Panel_info.setObjectName("Upadte_Panel_info")
        Upadte_Panel_info.resize(400, 212)
        self.label = QtWidgets.QLabel(Upadte_Panel_info)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.new_number_value = QtWidgets.QLineEdit(Upadte_Panel_info)
        self.new_number_value.setGeometry(QtCore.QRect(60, 70, 181, 21))
        self.new_number_value.setObjectName("new_number_value")
        self.Ok_button = QtWidgets.QPushButton(Upadte_Panel_info)
        self.Ok_button.setGeometry(QtCore.QRect(40, 150, 93, 28))
        self.Ok_button.setObjectName("Ok_button")
        self.Cancel_button = QtWidgets.QPushButton(Upadte_Panel_info)
        self.Cancel_button.setGeometry(QtCore.QRect(260, 150, 93, 28))
        self.Cancel_button.setObjectName("Cancel_button")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.retranslateUi(Upadte_Panel_info)
        QtCore.QMetaObject.connectSlotsByName(Upadte_Panel_info)

    def retranslateUi(self, Upadte_Panel_info):
        _translate = QtCore.QCoreApplication.translate
        Upadte_Panel_info.setWindowTitle(_translate("Upadte_Panel_info", "重新编号"))
        self.label.setText(_translate("Upadte_Panel_info", "请输入新的编号："))
        self.Ok_button.setText(_translate("Upadte_Panel_info", "确定"))
        self.Cancel_button.setText(_translate("Upadte_Panel_info", "取消"))
