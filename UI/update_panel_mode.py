# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_panel_mode.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Update_Panel_Model(object):
    def setupUi(self, Update_Panel_Model):
        Update_Panel_Model.setObjectName("Update_Panel_Model")
        Update_Panel_Model.resize(500, 600)
        self.panel_model_2 = QtWidgets.QLabel(Update_Panel_Model)
        self.panel_model_2.setGeometry(QtCore.QRect(50, 190, 80, 21))
        self.panel_model_2.setObjectName("panel_model_2")
        self.panel_m_power = QtWidgets.QLineEdit(Update_Panel_Model)
        self.panel_m_power.setGeometry(QtCore.QRect(190, 190, 251, 25))
        self.panel_m_power.setObjectName("panel_m_power")
        self.panel_model_7 = QtWidgets.QLabel(Update_Panel_Model)
        self.panel_model_7.setGeometry(QtCore.QRect(50, 140, 80, 21))
        self.panel_model_7.setObjectName("panel_model_7")
        self.btn_panel_m_color = QtWidgets.QPushButton(Update_Panel_Model)
        self.btn_panel_m_color.setGeometry(QtCore.QRect(190, 440, 150, 25))
        self.btn_panel_m_color.setObjectName("btn_panel_m_color")
        self.panel_model_4 = QtWidgets.QLabel(Update_Panel_Model)
        self.panel_model_4.setGeometry(QtCore.QRect(50, 290, 80, 21))
        self.panel_model_4.setObjectName("panel_model_4")
        self.panel_m_altitude = QtWidgets.QLineEdit(Update_Panel_Model)
        self.panel_m_altitude.setGeometry(QtCore.QRect(190, 290, 251, 25))
        self.panel_m_altitude.setObjectName("panel_m_altitude")
        self.panel_m_arrange = QtWidgets.QLineEdit(Update_Panel_Model)
        self.panel_m_arrange.setGeometry(QtCore.QRect(190, 390, 251, 25))
        self.panel_m_arrange.setObjectName("panel_m_arrange")
        self.btu_new_close = QtWidgets.QPushButton(Update_Panel_Model)
        self.btu_new_close.setGeometry(QtCore.QRect(300, 500, 93, 28))
        self.btu_new_close.setObjectName("btu_new_close")
        self.panel_model_18 = QtWidgets.QLabel(Update_Panel_Model)
        self.panel_model_18.setGeometry(QtCore.QRect(50, 40, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.panel_model_18.setFont(font)
        self.panel_model_18.setObjectName("panel_model_18")
        self.panel_m_color = QtWidgets.QWidget(Update_Panel_Model)
        self.panel_m_color.setGeometry(QtCore.QRect(350, 440, 91, 25))
        self.panel_m_color.setObjectName("panel_m_color")
        self.panel_model_8 = QtWidgets.QLabel(Update_Panel_Model)
        self.panel_model_8.setGeometry(QtCore.QRect(50, 390, 80, 21))
        self.panel_model_8.setObjectName("panel_model_8")
        self.panel_model_19 = QtWidgets.QLabel(Update_Panel_Model)
        self.panel_model_19.setGeometry(QtCore.QRect(50, 440, 80, 21))
        self.panel_model_19.setObjectName("panel_model_19")
        self.but_new_save = QtWidgets.QPushButton(Update_Panel_Model)
        self.but_new_save.setGeometry(QtCore.QRect(140, 500, 93, 28))
        self.but_new_save.setObjectName("but_new_save")
        self.but_delete = QtWidgets.QPushButton(Update_Panel_Model)
        self.but_delete.setGeometry(QtCore.QRect(140, 500, 93, 28))
        self.but_delete.setObjectName("but_delete")
        self.panel_m_wh = QtWidgets.QLineEdit(Update_Panel_Model)
        self.panel_m_wh.setGeometry(QtCore.QRect(190, 240, 251, 25))
        self.panel_m_wh.setObjectName("panel_m_wh")
        self.panel_model_6 = QtWidgets.QLabel(Update_Panel_Model)
        self.panel_model_6.setGeometry(QtCore.QRect(50, 90, 80, 21))
        self.panel_model_6.setObjectName("panel_model_6")
        self.panel_m_manufactor = QtWidgets.QLineEdit(Update_Panel_Model)
        self.panel_m_manufactor.setGeometry(QtCore.QRect(190, 140, 251, 25))
        self.panel_m_manufactor.setObjectName("panel_m_manufactor")
        self.panel_m_type = QtWidgets.QComboBox(Update_Panel_Model)
        self.panel_m_type.setGeometry(QtCore.QRect(190, 90, 251, 25))
        self.panel_m_type.setObjectName("panel_m_type")
        self.panel_m_angle = QtWidgets.QLineEdit(Update_Panel_Model)
        self.panel_m_angle.setGeometry(QtCore.QRect(190, 340, 251, 25))
        self.panel_m_angle.setObjectName("panel_m_angle")
        self.panel_model_3 = QtWidgets.QLabel(Update_Panel_Model)
        self.panel_model_3.setGeometry(QtCore.QRect(50, 240, 80, 21))
        self.panel_model_3.setObjectName("panel_model_3")
        self.panel_model_5 = QtWidgets.QLabel(Update_Panel_Model)
        self.panel_model_5.setGeometry(QtCore.QRect(50, 340, 80, 21))
        self.panel_model_5.setObjectName("panel_model_5")
        self.panel_model = QtWidgets.QComboBox(Update_Panel_Model)
        self.panel_model.setGeometry(QtCore.QRect(190, 40, 251, 25))
        self.panel_model.setObjectName("panel_model")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.retranslateUi(Update_Panel_Model)
        self.btu_new_close.clicked.connect(Update_Panel_Model.close)
        QtCore.QMetaObject.connectSlotsByName(Update_Panel_Model)

    def retranslateUi(self, Update_Panel_Model):
        _translate = QtCore.QCoreApplication.translate
        Update_Panel_Model.setWindowTitle(_translate("Update_Panel_Model", "修改模板信息"))
        self.panel_model_2.setText(_translate("Update_Panel_Model", "组件功率:"))
        self.panel_model_7.setText(_translate("Update_Panel_Model", "组件厂家:"))
        self.btn_panel_m_color.setText(_translate("Update_Panel_Model", "请选择颜色"))
        self.panel_model_4.setText(_translate("Update_Panel_Model", "组件海拔:"))
        self.btu_new_close.setText(_translate("Update_Panel_Model", "取消"))
        self.panel_model_18.setText(_translate("Update_Panel_Model", "组件型号:"))
        self.panel_model_8.setText(_translate("Update_Panel_Model", "组件排布:"))
        self.panel_model_19.setText(_translate("Update_Panel_Model", "选择颜色:"))
        self.but_new_save.setText(_translate("Update_Panel_Model", "保存"))
        self.but_delete.setText(_translate("Update_Panel_Model","删除模板"))
        self.panel_model_6.setText(_translate("Update_Panel_Model", "标注类型:"))
        self.panel_model_3.setText(_translate("Update_Panel_Model", "组件宽高:"))
        self.panel_model_5.setText(_translate("Update_Panel_Model", "组件角度:"))