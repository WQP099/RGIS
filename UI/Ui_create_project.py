# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythonWork\RGIS\UI\create_project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_creatProject(object):
    def setupUi(self, creatProject):
        creatProject.setObjectName("creatProject")
        creatProject.resize(392, 208)
        self.lab_projectTime = QtWidgets.QLabel(creatProject)
        self.lab_projectTime.setGeometry(QtCore.QRect(0, 10, 401, 20))
        self.lab_projectTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_projectTime.setObjectName("lab_projectTime")
        self.label_2 = QtWidgets.QLabel(creatProject)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 72, 15))
        self.label_2.setObjectName("label_2")
        self.le_projectName = QtWidgets.QLineEdit(creatProject)
        self.le_projectName.setGeometry(QtCore.QRect(120, 40, 251, 21))
        self.le_projectName.setObjectName("le_projectName")
        self.but_create = QtWidgets.QPushButton(creatProject)
        self.but_create.setGeometry(QtCore.QRect(50, 150, 93, 28))
        self.but_create.setObjectName("but_create")
        self.btu_close = QtWidgets.QPushButton(creatProject)
        self.btu_close.setGeometry(QtCore.QRect(210, 150, 93, 28))
        self.btu_close.setObjectName("btu_close")
        self.but_map_path = QtWidgets.QPushButton(creatProject)
        self.but_map_path.setGeometry(QtCore.QRect(10, 70, 91, 28))
        self.but_map_path.setObjectName("but_map_path")
        self.le_map_path = QtWidgets.QLineEdit(creatProject)
        self.le_map_path.setGeometry(QtCore.QRect(120, 70, 251, 21))
        self.le_map_path.setObjectName("le_map_path")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.retranslateUi(creatProject)
        self.btu_close.clicked.connect(creatProject.close)
        QtCore.QMetaObject.connectSlotsByName(creatProject)

    def retranslateUi(self, creatProject):
        _translate = QtCore.QCoreApplication.translate
        creatProject.setWindowTitle(_translate("creatProject", "创建项目"))
        self.lab_projectTime.setText(_translate("creatProject", "项目创建时间"))
        self.label_2.setText(_translate("creatProject", "项目名称："))
        self.but_create.setText(_translate("creatProject", "创建"))
        self.btu_close.setText(_translate("creatProject", "取消"))
        self.but_map_path.setText(_translate("creatProject", "选择全景图1"))
