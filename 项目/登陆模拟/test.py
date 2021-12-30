from yolov4_login.facedet import FaceDetector
import cv2

detector = FaceDetector()
img = cv2.imread("IMG_1099.jpg")
img = detector.detect_mark(img)

cv2.imwrite("dd.png", img)