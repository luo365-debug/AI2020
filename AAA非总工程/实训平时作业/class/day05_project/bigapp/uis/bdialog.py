from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPainter
from bigapp.ais.bfish import BFish
from PyQt5.QtCore import Qt

class BDialog(QDialog):
    def _init_(self):
        super(BDialog,self)._init_()

        
        self.fish=BFish()
        self.fish.signal_open.connect(self.repaint)
        self.fish.start()

        self.fish2=BFish()
        self.fish2.signal_open.connect(self.repaint)
        self.fish2.start()

    def keyPressEvent(self,e):
        #键盘按键处理
        key = e.key()
        if key == Qt.Key_Right:
            self.fish2.change_dir(0)
            self.fish2.swim()
        if key == Qt.Key_Up:
            self.fish2.change_dir(90)
            self.fish2.swim()
        if key == Qt.Key_Left:
            self.fish2.change_dir(180)
            self.fish2.swim()
        if key == Qt.Key_Down:
            self.fish2.change_dir(270)
            self.fish2.swim()

    def paintEvent(self,e):
        #print("窗体在绘制")
        paiter=QPainter(self)

        self.fish.show_me(painter)
