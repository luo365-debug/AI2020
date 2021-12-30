from PyQt5.QtWidgets import QDialog
from xxxapp.guis.login.loginui import Ui_Login
"""
https://doc.qt.io/qt-5/stylesheet-reference.html
"""
class XXXLogin(QDialog):

    def __init__(self):
        super(XXXLogin, self).__init__()
        self.ui_login = Ui_Login()
        self.ui_login.setupUi(self)
        