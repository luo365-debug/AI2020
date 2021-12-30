from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(799, 552)
        Login.setStyleSheet("QLabel#lbl_face_video{\n"
"    border-top-color:#BBBBBB;\n"
"    border-right-color:#BBBBBB;\n"
"    border-bottom-color:#FFFFFF;\n"
"    border-left-color:#FFFFFF;\n"
"    border-style:solid;\n"
"    border-width: 3px;\n"
"    border-radius:20px;\n"
"}")
        self.lbl_title = QtWidgets.QLabel(Login)
        self.lbl_title.setGeometry(QtCore.QRect(220, 30, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_version = QtWidgets.QLabel(Login)
        self.lbl_version.setGeometry(QtCore.QRect(360, 110, 68, 20))
        self.lbl_version.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.lbl_subtitle = QtWidgets.QLabel(Login)
        self.lbl_subtitle.setGeometry(QtCore.QRect(320, 150, 141, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_subtitle.setFont(font)
        self.lbl_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_subtitle.setObjectName("lbl_subtitle")
        self.line = QtWidgets.QFrame(Login)
        self.line.setGeometry(QtCore.QRect(250, 100, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lbl_face_video = QtWidgets.QLabel(Login)
        self.lbl_face_video.setGeometry(QtCore.QRect(130, 230, 531, 271))
        self.lbl_face_video.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_face_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_face_video.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_face_video.setObjectName("lbl_face_video")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "交通标志智能识别系统 - 智能登录 "))
        self.lbl_title.setText(_translate("Login", "交通标志智能识别系统"))
        self.lbl_version.setText(_translate("Login", "v1.0"))
        self.lbl_subtitle.setText(_translate("Login", "系统智能登录"))
        self.lbl_face_video.setText(_translate("Login", "人脸登录界面"))
