from PyQt5.QtCore import QThread, pyqtSignal
import cv2
from yolov4_traffic.trafficdet import TrafficDetector
# yolov4_login.facedet import FaceDetector
from trafficapp.biz.home.users import UserDAO

class TrafficThread(QThread):
    """
        int: 图像高度
        int：图像宽度
        int：图像的通道
        bytes：图像的二进制数据
        bool: 是否识别成功
    """
    signal_traffic = pyqtSignal(int, int, int, bytes, bool) 
    def __init__(self):
        super(TrafficThread, self).__init__()
        self.dev = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.is_ok = False
        # 构建一个智能侦测对象
        self.detector = TrafficDetector()
        # 识别结果存储
        self.users = []
        self.counter = 0
        # 数据验证模块
        self.dao = UserDAO()

    def run(self):
        while not self.is_ok:
        #while True:
            # 采集视频
            status, frame = self.dev.read()
            if not status:
                self.is_ok = True
                print("无法获得图像")
                continue
            # 发送信号
            h, w, c = frame.shape
            # 做登录检测，与验证，
            home_ok = False

            pred = self.detector.detect(frame)
            if pred is not None:
                # 循环处理识别结果
                for x1, y1, x2, y2, p, cls_id in pred:
                    # 概率过滤
                    if p > 0.5:
                        cls_id = int(cls_id)
                        name = self.detector.get_name(cls_id)
                        self.users.append(name)
                        self.counter += 1
                        # 实现标注
                        x1 = int(x1)
                        y1 = int(y1)
                        x2 = int(x2)
                        y2 = int(y2)
                        cv2.rectangle(frame, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=4)
                        cv2.putText(
                            frame, 
                            F"{name}:{p:.2f}", 
                            org=(x1, y1 - 50 ), 
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=0.5,
                            color=(0, 255, 255),
                            thickness=1)
            if self.counter >= 10:
                # 验证/先取识别最多的标志
                most_name = max(self.users, key=self.users.count)
                # 调用业务模块，验证
                home_ok = self.dao.validate(most_name)
                self.counter = 0
                self.users = [] 
            frame = frame[:,:,::-1]
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.signal_traffic.emit(h, w, c, frame.tobytes(), home_ok)
            QThread.usleep(100000)

