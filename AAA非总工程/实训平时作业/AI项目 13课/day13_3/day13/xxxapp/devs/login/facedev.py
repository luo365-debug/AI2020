from PyQt5.QtCore import QThread, pyqtSignal
import cv2

class FaceThread(QThread):
    """
        int: 图像高度
        int：图像宽度
        int：图像的通道
        bytes：图像的二进制数据
        bool: 是否登录成功
    """
    signal_face = pyqtSignal(int, int, int, bytes, bool) 
    def __init__(self):
        super(FaceThread, self).__init__()
        self.dev = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.is_ok = False

    def run(self):
        while not self.is_ok:
            # 采集视频
            status, frame = self.dev.read()
            if not status:
                self.is_ok = True
                continue
            # 发送信号
            h, w, c = frame.shape
            # 做登录检测，与验证，
            login_ok = False
            # frame = frame[:,:,::-1]
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.signal_face.emit(h, w, c, frame.tobytes(), login_ok)
            QThread.usleep(100000)

    def close(self):
        self.is_ok=True
        # 结束线程-暴力型
        self.terminate()
        # while isRunning():
        #     pass
        # 释放设备
        self.dev.release()
