from PyQt5.QtCore import QThread,pyqtSignal,Qt
from PyQt5.QtGui import QPen,QColor

class BFish(QThread):
    sign_open=pyqtSignal()

    def _init_(self):
        super(BFish,self)._init_()
        self.x=100#初始位置
        self.y=100
        self.s=200#大小
        self.d=0#方向
        self.m=45
        self.is_open=1#张嘴与否

    #移动
    def swim(self):
        if self.d==0:# →
            self.x+=1
        elif self.d==90:# ↑
            self.y-=1
        elif self.d==180:# ←
            self.x-=1
        elif self.d==270:# ↓
            self.y+=1

    #是否张嘴
    def open_mouth(self):
        if self.is_open:
            self.m += 5
            if self.m >=45:
                self.is_open = not self.is_open
                self.m = 45
        else:
            self.m -= 5
            if self.m <= 0:
                self.is_open = not self.is_open
                self.m = 0

    def show_me(self,g):
        color=QColor(255,0,0)#颜色
        pen=QPen(color,4.0,Qt.DashDotLine)#画笔线条
        g.drawPie(
            self.x,self.y,
            self.s,self.s,
            (self.m+self.d)*16,
            (360-2*self.m)*16
        )   
    
    def run(self):
        while True:
            self.open_mouth()
            self.signal_open.emit()
            QThread.usleep(100000)