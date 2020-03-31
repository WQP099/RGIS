from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
class Ui_Loading_object(object):
    def setupUi(self, Ui_Loading):
        Ui_Loading.setObjectName("Ui_Loading")
        Ui_Loading.resize(500, 300)

        self.label = QtWidgets.QLabel(Ui_Loading)

        self.label.setGeometry(QtCore.QRect(0, 0, 500, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        self.retranslateUi(Ui_Loading)

        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        QtCore.QMetaObject.connectSlotsByName(Ui_Loading)



    def retranslateUi(self, Ui_Loading):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Ui_Loading", "正在上传，请等待..."))