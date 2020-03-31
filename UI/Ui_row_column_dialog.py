# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'row_column_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_row_Column_Dialog(object):
    def setupUi(self, row_Column_Dialog):
        row_Column_Dialog.setObjectName("row_Column_Dialog")
        row_Column_Dialog.resize(400, 238)
        self.ok_row_column_btn = QtWidgets.QPushButton(row_Column_Dialog)
        self.ok_row_column_btn.setGeometry(QtCore.QRect(40, 190, 93, 28))
        self.ok_row_column_btn.setObjectName("ok_row_column_btn")
        self.cancel_row_column_btn = QtWidgets.QPushButton(row_Column_Dialog)
        self.cancel_row_column_btn.setGeometry(QtCore.QRect(260, 190, 93, 28))
        self.cancel_row_column_btn.setObjectName("cancel_row_column_btn")
        self.label = QtWidgets.QLabel(row_Column_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 153, 33))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(row_Column_Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 153, 33))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.row_num_value = QtWidgets.QLineEdit(row_Column_Dialog)
        self.row_num_value.setGeometry(QtCore.QRect(70, 60, 181, 20))
        self.row_num_value.setObjectName("row_num_value")
        self.row_num_value.setValidator(QtGui.QIntValidator())
        self.column_num_value = QtWidgets.QLineEdit(row_Column_Dialog)
        self.column_num_value.setGeometry(QtCore.QRect(70, 130, 181, 20))
        self.column_num_value.setObjectName("column_num_value")
        self.column_num_value.setValidator(QtGui.QIntValidator())
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.retranslateUi(row_Column_Dialog)

        QtCore.QMetaObject.connectSlotsByName(row_Column_Dialog)

    def retranslateUi(self, row_Column_Dialog):
        _translate = QtCore.QCoreApplication.translate
        row_Column_Dialog.setWindowTitle(_translate("row_Column_Dialog", "Dialog"))
        self.ok_row_column_btn.setText(_translate("row_Column_Dialog", "确定"))
        self.cancel_row_column_btn.setText(_translate("row_Column_Dialog", "取消"))
        self.label.setText(_translate("row_Column_Dialog", "请输入整行数量："))
        self.label_2.setText(_translate("row_Column_Dialog", "请输入整列数量："))
