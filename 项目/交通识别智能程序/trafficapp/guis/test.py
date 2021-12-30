from PyQt5.QtWidgets import QApplication
import sys
#from trafficapp.guis.login.trafficlogin import TrafficLogin
from trafficapp.guis.home.traffichome import TrafficHome 

class TrafficApp(QApplication):
    def __init__(self):
        super(TrafficApp, self).__init__(sys.argv)
        #self.login = TrafficLogin()
        self.home = TrafficHome()

        #self.login.signal_home.connect(self.recv_login_info)
        #self.login.show()

    #def recv_login_info(self):
        
        self.home.show()
        #self.login.destroy()