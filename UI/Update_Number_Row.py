# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Update_Number_Row.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Update_number_Dialog(object):
    def setupUi(self, Update_number_Dialog):
        Update_number_Dialog.setObjectName("Update_number_Dialog")
        Update_number_Dialog.resize(585, 411)
        self.label = QtWidgets.QLabel(Update_number_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Number_value = QtWidgets.QLineEdit(Update_number_Dialog)
        self.Number_value.setGeometry(QtCore.QRect(70, 70, 181, 25))
        self.Number_value.setObjectName("Number_value")
        self.Ok_button = QtWidgets.QPushButton(Update_number_Dialog)
        self.Ok_button.setGeometry(QtCore.QRect(100, 320, 93, 28))
        self.Ok_button.setObjectName("Ok_button")
        self.Cancel_button = QtWidgets.QPushButton(Update_number_Dialog)
        self.Cancel_button.setGeometry(QtCore.QRect(320, 320, 93, 28))
        self.Cancel_button.setObjectName("Cancel_button")
        self.label_2 = QtWidgets.QLabel(Update_number_Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 511, 42))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Update_number_Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.number_direction = QtWidgets.QComboBox(Update_number_Dialog)
        self.number_direction.setGeometry(QtCore.QRect(70, 220, 181, 25))
        self.number_direction.setObjectName("number_direction")
        self.number_direction.addItem("")
        self.number_direction.addItem("")
        self.number_direction.addItem("")
        self.number_direction.addItem("")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.retranslateUi(Update_number_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Update_number_Dialog)

    def retranslateUi(self, Update_number_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Update_number_Dialog.setWindowTitle(_translate("Update_number_Dialog", "重新编号"))
        self.label.setText(_translate("Update_number_Dialog", "请输入单行编号格式："))
        self.Number_value.setPlaceholderText(_translate("Update_number_Dialog", "0,0,0 "))
        self.Ok_button.setText(_translate("Update_number_Dialog", "确定"))
        self.Cancel_button.setText(_translate("Update_number_Dialog", "取消"))
        self.label_2.setText(_translate("Update_number_Dialog", "提示*：请输入左下角组件编号,\n       第一位是区域编号，第二位为行编号 ，第三位为列编号"))
        self.label_3.setText(_translate("Update_number_Dialog", "编号方向："))
        self.number_direction.setCurrentText(_translate("Update_number_Dialog", "右增上增"))
        self.number_direction.setItemText(0, _translate("Update_number_Dialog", "右增上增"))
        self.number_direction.setItemText(1, _translate("Update_number_Dialog", "右减上增"))
        self.number_direction.setItemText(2, _translate("Update_number_Dialog", "右增上减"))
        self.number_direction.setItemText(3, _translate("Update_number_Dialog", "右减上减"))
