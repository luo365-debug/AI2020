from yolov4_traffic.trafficdet import TrafficDetector
import cv2

detector = TrafficDetector()
img = cv2.imread("00776.png")
img = detector.detect_mark(img)

cv2.imwrite("home.png", img)