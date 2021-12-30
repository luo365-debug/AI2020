from yolov4.facedet import FaceDetector
import cv2

detector = FaceDetector()
img = cv2.imread("IMG_3048.JPG")
img = detector.detect_mark(img)
cv2.imwrite("dd.png",img)