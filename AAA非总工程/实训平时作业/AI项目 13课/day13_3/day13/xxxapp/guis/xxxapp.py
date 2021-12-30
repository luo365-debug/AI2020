from PyQt5.QtWidgets import QApplication
import sys
from xxxapp.guis.login.xxxlogin import XXXLogin
from xxxapp.guis.home.xxxhome import XXXHome 

class XXXApp(QApplication):
    def __init__(self):
        super(XXXApp, self).__init__(sys.argv)
        self.login = XXXLogin()
        self.home = XXXHome()
        # self.home.hide()  # 对话框默认隐藏
        self.login.show()
        # self.home.show()  # 一定等登录成功才显示
