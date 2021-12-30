import numpy
import cv2

img=cv2.imread("00016.JPG")

print(img[1])#取一行
print(img[1,1])#某行某列的一个像素  [x,y,z] z是该像素的一个颜色通道

#数组下标 [] 右取值 左赋值

img[100]=255#把第100行改成255颜色
#img[:,:,0]=0

img[img[:,:,0]>100]=0#把一片像素修改  [begin:end:step]
cv2.imwrite("dd.png",img)
