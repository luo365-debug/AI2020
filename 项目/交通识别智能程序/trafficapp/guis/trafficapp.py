from PyQt5.QtWidgets import QApplication
import sys
from trafficapp.guis.login.trafficlogin import TrafficLogin
from trafficapp.guis.home.traffichome import TrafficHome 

class TrafficApp(QApplication):
    def __init__(self):
        super(TrafficApp, self).__init__(sys.argv)
        self.login = TrafficLogin()
        self.home = TrafficHome()
        # self.home.hide()  # 对话框默认隐藏
        self.login.signal_home.connect(self.recv_login_info)
        self.login.show()
        # self.home.show()  # 一定等登录成功才显示

    def recv_login_info(self):
        # print("登录成功，启动系统的主界面")
        self.login.destroy()
        self.home.init_dev()
        self.home.show()
        