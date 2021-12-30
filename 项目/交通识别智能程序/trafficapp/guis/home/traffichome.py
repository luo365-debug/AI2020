from PyQt5.QtWidgets import QDialog
from trafficapp.guis.home.homeui import Ui_Video
from trafficapp.devs.home.homedev import TrafficThread
#from trafficapp.devs.login.facedev import FaceThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal, Qt

class TrafficHome(QDialog):

    def __init__(self):
        super(TrafficHome, self).__init__()
        self.ui_home=Ui_Video()
        self.ui_home.setupUi(self)

    def init_dev(self):
        # 视频采集任务线程
        self.home_th = TrafficThread()
        self.home_th.signal_traffic.connect(self.show_login_video)
        self.home_th.start()

    def show_login_video(self, h, w, c, data, login_ok):
            # 显示图像
            qimg = QImage(data, w, h, w * c, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimg)
            self.ui_home.lbl_traffic.setPixmap(pixmap)
            self.ui_home.lbl_traffic.setScaledContents(True) 
