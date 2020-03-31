# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload_chain.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Chain_object(object):
    def setupUi(self, Chain_object):
        Chain_object.setObjectName("Chain_object")
        Chain_object.resize(1090, 782)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Chain_object)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1091, 721))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.local_project_info_layout = QtWidgets.QVBoxLayout()
        self.local_project_info_layout.setContentsMargins(20, -1, 20, -1)
        self.local_project_info_layout.setObjectName("local_project_info_layout")
        self.local_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.local_label.setFont(font)
        self.local_label.setAlignment(QtCore.Qt.AlignCenter)
        self.local_label.setObjectName("local_label")
        self.local_project_info_layout.addWidget(self.local_label)
        self.local_list = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.local_list.setFont(font)
        self.local_list.setObjectName("local_list")
        self.local_project_info_layout.addWidget(self.local_list)
        self.horizontalLayout.addLayout(self.local_project_info_layout)
        self.chain_project_layout = QtWidgets.QVBoxLayout()
        self.chain_project_layout.setContentsMargins(20, -1, 20, -1)
        self.chain_project_layout.setObjectName("chain_project_layout")
        self.chain_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chain_label.setFont(font)
        self.chain_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chain_label.setAlignment(QtCore.Qt.AlignCenter)
        self.chain_label.setObjectName("chain_label")
        self.chain_project_layout.addWidget(self.chain_label)
        self.chain_list = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.chain_list.setObjectName("chain_list")
        self.chain_project_layout.addWidget(self.chain_list)
        self.horizontalLayout.addLayout(self.chain_project_layout)
        self.btu_close = QtWidgets.QPushButton(Chain_object)
        self.btu_close.setGeometry(QtCore.QRect(580, 740, 93, 28))
        self.btu_close.setObjectName("btu_close")
        self.btn_upload = QtWidgets.QPushButton(Chain_object)
        self.btn_upload.setGeometry(QtCore.QRect(440, 740, 93, 28))
        self.btn_upload.setObjectName("btn_upload")

        self.retranslateUi(Chain_object)
        QtCore.QMetaObject.connectSlotsByName(Chain_object)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def retranslateUi(self, Chain_object):
        _translate = QtCore.QCoreApplication.translate
        Chain_object.setWindowTitle(_translate("Chain_object", "区块链上传"))
        self.local_label.setText(_translate("Chain_object", "本地项目"))
        self.chain_label.setText(_translate("Chain_object", "云平台项目"))
        self.btu_close.setText(_translate("Chain_object", "取消"))
        self.btn_upload.setText(_translate("Chain_object", "上传"))
