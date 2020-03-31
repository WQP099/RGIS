# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythonWork\RGIS\UI\set_panel_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setPanelInfo(object):
    def setupUi(self, setPanelInfo):
        setPanelInfo.setObjectName("setPanelInfo")
        setPanelInfo.resize(430, 457)
        self.panel_model = QtWidgets.QLabel(setPanelInfo)
        self.panel_model.setGeometry(QtCore.QRect(20, 110, 105, 17))
        self.panel_model.setObjectName("panel_model")
        self.le_panel_model = QtWidgets.QLineEdit(setPanelInfo)
        self.le_panel_model.setGeometry(QtCore.QRect(100, 110, 251, 21))
        self.le_panel_model.setObjectName("le_panel_model")
        self.but_save = QtWidgets.QPushButton(setPanelInfo)
        self.but_save.setGeometry(QtCore.QRect(50, 360, 93, 28))
        self.but_save.setObjectName("but_save")
        self.btu_close = QtWidgets.QPushButton(setPanelInfo)
        self.btu_close.setGeometry(QtCore.QRect(210, 360, 93, 28))
        self.btu_close.setObjectName("btu_close")
        self.panel_model_2 = QtWidgets.QLabel(setPanelInfo)
        self.panel_model_2.setGeometry(QtCore.QRect(20, 150, 105, 17))
        self.panel_model_2.setObjectName("panel_model_2")
        self.panel_model_3 = QtWidgets.QLabel(setPanelInfo)
        self.panel_model_3.setGeometry(QtCore.QRect(20, 190, 105, 17))
        self.panel_model_3.setObjectName("panel_model_3")
        self.panel_model_4 = QtWidgets.QLabel(setPanelInfo)
        self.panel_model_4.setGeometry(QtCore.QRect(20, 230, 105, 17))
        self.panel_model_4.setObjectName("panel_model_4")
        self.panel_model_5 = QtWidgets.QLabel(setPanelInfo)
        self.panel_model_5.setGeometry(QtCore.QRect(20, 270, 105, 17))
        self.panel_model_5.setObjectName("panel_model_5")
        self.le_panel_power = QtWidgets.QLineEdit(setPanelInfo)
        self.le_panel_power.setGeometry(QtCore.QRect(100, 150, 251, 21))
        self.le_panel_power.setObjectName("le_panel_power")
        self.le_panel_wh = QtWidgets.QLineEdit(setPanelInfo)
        self.le_panel_wh.setGeometry(QtCore.QRect(100, 190, 251, 21))
        self.le_panel_wh.setObjectName("le_panel_wh")
        self.le_panel_altitude = QtWidgets.QLineEdit(setPanelInfo)
        self.le_panel_altitude.setGeometry(QtCore.QRect(100, 230, 251, 21))
        self.le_panel_altitude.setObjectName("le_panel_altitude")
        self.le_panel_angle = QtWidgets.QLineEdit(setPanelInfo)
        self.le_panel_angle.setGeometry(QtCore.QRect(100, 270, 251, 21))
        self.le_panel_angle.setObjectName("le_panel_angle")
        self.panel_model_6 = QtWidgets.QLabel(setPanelInfo)
        self.panel_model_6.setGeometry(QtCore.QRect(20, 30, 105, 17))
        self.panel_model_6.setObjectName("panel_model_6")
        #self.le_label_type = QtWidgets.QLineEdit(setPanelInfo)
        self.le_label_type = QtWidgets.QComboBox(setPanelInfo)
        self.le_label_type.setGeometry(QtCore.QRect(100, 30, 251, 21))
        self.le_label_type.setObjectName("le_label_type")

        self.le_label_manufactor = QtWidgets.QLineEdit(setPanelInfo)
        self.le_label_manufactor.setGeometry(QtCore.QRect(100, 70, 251, 21))
        self.le_label_manufactor.setObjectName("le_label_manufactor")
        self.panel_model_7 = QtWidgets.QLabel(setPanelInfo)
        self.panel_model_7.setGeometry(QtCore.QRect(20, 70, 105, 17))
        self.panel_model_7.setObjectName("panel_model_7")
        self.le_panel_arrange = QtWidgets.QLineEdit(setPanelInfo)
        self.le_panel_arrange.setGeometry(QtCore.QRect(100, 310, 251, 21))
        self.le_panel_arrange.setObjectName("le_panel_arrange")
        self.panel_model_8 = QtWidgets.QLabel(setPanelInfo)
        self.panel_model_8.setGeometry(QtCore.QRect(20, 310, 105, 17))
        self.panel_model_8.setObjectName("panel_model_8")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.retranslateUi(setPanelInfo)
        self.btu_close.clicked.connect(setPanelInfo.close)
        QtCore.QMetaObject.connectSlotsByName(setPanelInfo)

    def retranslateUi(self, setPanelInfo):
        _translate = QtCore.QCoreApplication.translate
        setPanelInfo.setWindowTitle(_translate("setPanelInfo", "设置组件信息"))
        self.panel_model.setText(_translate("setPanelInfo", "组件型号:"))
        self.but_save.setText(_translate("setPanelInfo", "保存"))
        self.btu_close.setText(_translate("setPanelInfo", "取消"))
        self.panel_model_2.setText(_translate("setPanelInfo", "组件功率:"))
        self.panel_model_3.setText(_translate("setPanelInfo", "组件宽高:"))
        self.panel_model_4.setText(_translate("setPanelInfo", "组件海拔:"))
        self.panel_model_5.setText(_translate("setPanelInfo", "组件角度:"))
        self.panel_model_6.setText(_translate("setPanelInfo", "标注类型:"))
        self.panel_model_7.setText(_translate("setPanelInfo", "组件厂家:"))
        self.panel_model_8.setText(_translate("setPanelInfo", "组件排布:"))
