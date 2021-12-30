import numpy
import cv2

#img=numpy.ndarray(shape=(500,500,3),dtype=numpy.uint8)
#img.fill(255)#填充颜色
#cv2.imwrite("dd.png",img)#把img存入名为dd的png格式图片中

arr=[[255 for x in range(500)]for y in range(500)]#二维数组
#255可改成[255,0,0,10]其中10表示透明度     [255,0,0]纯色
img=numpy.array(arr)
cv2.imwrite("dd.png",img)