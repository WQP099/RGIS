# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_select_panel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_update_Panel(object):
    def setupUi(self, update_Panel):
        update_Panel.setObjectName("update_Panel")
        update_Panel.resize(500, 520)
        #组件名称
        self.panel_model_6 = QtWidgets.QLabel(update_Panel)
        self.panel_model_6.setGeometry(QtCore.QRect(30, 20, 105, 17))
        self.panel_model_6.setObjectName("panel_model_6")
        #组件厂家
        self.panel_model_9 = QtWidgets.QLabel(update_Panel)
        self.panel_model_9.setGeometry(QtCore.QRect(30, 60, 105, 17))
        self.panel_model_9.setObjectName("panel_model_7")
        #组件类型
        self.panel_model = QtWidgets.QLabel(update_Panel)
        self.panel_model.setGeometry(QtCore.QRect(30, 100, 105, 17))
        self.panel_model.setObjectName("panel_model")
        #组件型号
        self.panel_model_2 = QtWidgets.QLabel(update_Panel)
        self.panel_model_2.setGeometry(QtCore.QRect(30, 140, 105, 17))
        self.panel_model_2.setObjectName("panel_model_2")
        #组件功率
        self.panel_model_3 = QtWidgets.QLabel(update_Panel)
        self.panel_model_3.setGeometry(QtCore.QRect(30, 180, 105, 17))
        self.panel_model_3.setObjectName("panel_model_3")
        #组件宽高
        self.panel_model_4 = QtWidgets.QLabel(update_Panel)
        self.panel_model_4.setGeometry(QtCore.QRect(30, 220, 105, 17))
        self.panel_model_4.setObjectName("panel_model_4")
        #组件海拔
        self.panel_model_5 = QtWidgets.QLabel(update_Panel)
        self.panel_model_5.setGeometry(QtCore.QRect(30, 260, 105, 17))
        self.panel_model_5.setObjectName("panel_model_5")
        #组件角度
        self.panel_model_7 = QtWidgets.QLabel(update_Panel)
        self.panel_model_7.setGeometry(QtCore.QRect(30, 300, 105, 17))
        self.panel_model_7.setObjectName("panel_model_7")
        #组件排布
        self.panel_model_10 = QtWidgets.QLabel(update_Panel)
        self.panel_model_10.setGeometry(QtCore.QRect(30, 340, 100, 17))
        self.panel_model_10.setObjectName("panel_model_10")
        #GPS
        self.panel_model_8 = QtWidgets.QLabel(update_Panel)
        self.panel_model_8.setGeometry(QtCore.QRect(30, 380, 100, 17))
        self.panel_model_8.setObjectName("panel_model_8")

        self.btu_close = QtWidgets.QPushButton(update_Panel)
        self.btu_close.setGeometry(QtCore.QRect(270, 450, 93, 28))
        self.btu_close.setObjectName("btu_close")
        self.but_save = QtWidgets.QPushButton(update_Panel)
        self.but_save.setGeometry(QtCore.QRect(110, 450, 93, 28))
        self.but_save.setObjectName("but_save")
        #组件名称
        self.panel_info_name = QtWidgets.QLineEdit(update_Panel)
        self.panel_info_name.setGeometry(QtCore.QRect(150, 20, 251, 21))
        self.panel_info_name.setObjectName("panel_info_name")
        #组件厂家
        self.panel_info_manufactor = QtWidgets.QLineEdit(update_Panel)
        self.panel_info_manufactor.setGeometry(QtCore.QRect(150, 60, 251, 21))
        self.panel_info_manufactor.setObjectName("panel_info_manufactor")
        self.panel_info_manufactor.setEnabled(False)
        #标注类型
        self.panel_info_type = QtWidgets.QLineEdit(update_Panel)
        self.panel_info_type.setGeometry(QtCore.QRect(150, 100, 251, 21))
        self.panel_info_type.setObjectName("panel_info_type")
        self.panel_info_type.setEnabled(False)
        #组件型号
        self.panel_info_model = QtWidgets.QComboBox(update_Panel)
        self.panel_info_model.setGeometry(QtCore.QRect(150, 140, 251, 21))
        self.panel_info_model.setObjectName("panel_info_model")
        #组件功率
        self.panel_info_power = QtWidgets.QLineEdit(update_Panel)
        self.panel_info_power.setGeometry(QtCore.QRect(150, 180, 251, 21))
        self.panel_info_power.setObjectName("panel_info_power")
        self.panel_info_power.setEnabled(False)
        #组件宽高
        self.panel_info_wh = QtWidgets.QLineEdit(update_Panel)
        self.panel_info_wh.setGeometry(QtCore.QRect(150, 220, 251, 21))
        self.panel_info_wh.setObjectName("panel_info_wh")
        self.panel_info_wh.setEnabled(False)

        #组件海拔
        self.panel_info_altitude = QtWidgets.QLineEdit(update_Panel)
        self.panel_info_altitude.setGeometry(QtCore.QRect(150, 260, 251, 21))
        self.panel_info_altitude.setObjectName("panel_info_altitude")
        self.panel_info_altitude.setEnabled(False)
        #组件角度
        self.panel_info_angle = QtWidgets.QLineEdit(update_Panel)
        self.panel_info_angle.setGeometry(QtCore.QRect(150, 300, 251, 21))
        self.panel_info_angle.setObjectName("panel_info_angle")
        self.panel_info_angle.setEnabled(False)
        #组件排布
        self.panel_info_arrange = QtWidgets.QLineEdit(update_Panel)
        self.panel_info_arrange.setGeometry(QtCore.QRect(150, 340, 251, 21))
        self.panel_info_arrange.setObjectName("panel_info_arrange")
        self.panel_info_arrange.setText("2x10")
        self.panel_info_arrange.setEnabled(False)
        #GPS
        self.panel_info_GPS = QtWidgets.QLineEdit(update_Panel)
        self.panel_info_GPS.setGeometry(QtCore.QRect(150, 380, 251, 21))
        self.panel_info_GPS.setObjectName("panel_info_GPS")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.retranslateUi(update_Panel)

        QtCore.QMetaObject.connectSlotsByName(update_Panel)

    def retranslateUi(self, update_Panel):
        _translate = QtCore.QCoreApplication.translate
        update_Panel.setWindowTitle(_translate("update_Panel", "修改信息"))
        self.panel_model.setText(_translate("update_Panel", "标注类型:"))
        self.panel_model_5.setText(_translate("update_Panel", "组件海拔:"))
        self.panel_model_6.setText(_translate("update_Panel", "组件编号:"))
        self.panel_model_9.setText(_translate("update_Panel", "组件厂家:"))
        self.panel_model_2.setText(_translate("update_Panel", "组件型号:"))
        self.panel_model_4.setText(_translate("update_Panel", "组件宽高:"))
        self.panel_model_3.setText(_translate("update_Panel", "组件功率:"))
        self.panel_model_7.setText(_translate("update_Panel", "组件角度:"))
        self.panel_model_10.setText(_translate("update_Panel", "组件排布:"))
        self.panel_model_8.setText(_translate("update_Panel", "GPS(经,纬):"))
        self.btu_close.setText(_translate("update_Panel", "取消"))
        self.but_save.setText(_translate("update_Panel", "保存"))
