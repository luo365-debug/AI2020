from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Video(object):
    def setupUi(self, Video):
        Video.setObjectName("traffic")
        Video.resize(750, 500)
        
        self.lbl_traffic = QtWidgets.QLabel(Video)
        self.lbl_traffic.setGeometry(QtCore.QRect(0, 0, 750, 500))
        self.lbl_traffic.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_traffic.setObjectName("lbl_traffic")

        self.retranslateUi(Video)
        QtCore.QMetaObject.connectSlotsByName(Video)

    def retranslateUi(self, Video):
        _translate = QtCore.QCoreApplication.translate
        Video.setWindowTitle(_translate("traffic", "交通标识识别"))
        self.lbl_traffic.setText(_translate("traffic", "交通视频区域"))