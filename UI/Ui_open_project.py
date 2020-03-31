# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythonWork\RGIS\UI\open_project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_open_project(object):
    def setupUi(self, open_project):
        open_project.setObjectName("open_project")
        open_project.resize(488, 347)
        self.btu_close = QtWidgets.QPushButton(open_project)
        self.btu_close.setGeometry(QtCore.QRect(270, 300, 93, 28))
        self.btu_close.setObjectName("btu_close")
        self.but_open = QtWidgets.QPushButton(open_project)
        self.but_open.setGeometry(QtCore.QRect(130, 300, 93, 28))
        self.but_open.setObjectName("but_open")
        self.lw_local_PN = QtWidgets.QListWidget(open_project)
        self.lw_local_PN.setGeometry(QtCore.QRect(10, 40, 471, 251))
        self.lw_local_PN.setObjectName("lw_local_PN")
        self.label_3 = QtWidgets.QLabel(open_project)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 471, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.retranslateUi(open_project)
        self.btu_close.clicked.connect(open_project.close)
        QtCore.QMetaObject.connectSlotsByName(open_project)

    def retranslateUi(self, open_project):
        _translate = QtCore.QCoreApplication.translate
        open_project.setWindowTitle(_translate("open_project", "打开项目"))
        self.btu_close.setText(_translate("open_project", "取消"))
        self.but_open.setText(_translate("open_project", "打开"))
        self.label_3.setText(_translate("open_project", "已创建项目"))
