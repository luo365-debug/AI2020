import torch
from torchvision.datasets import MNIST  # 数据集(MNIST是一个手写数据集)
from torchvision.transforms import Compose, ToTensor # 转换操作
from torch.utils.data import DataLoader # 批次数据集(每次循环操作多张图片)
import numpy, cv2

# 1. 加载数据集
transform = Compose([ToTensor()])  # torch加载图像使用的是PIL图像库，定义一个转换
train_data = MNIST(root="data", download=True, train=True,  transform=transform)#加载训练集(train=true)
valid_data = MNIST(root="data", download=True, train=False, transform=transform) #加载验证集
                    #root路径，download=true时项目没有即下载第二个可T可F(第一个T)
# Dataset: __len__
print(len(train_data), len(valid_data))
# Dataset: 下标运算
image, label = train_data[0]#image图像，label标签
print(image.shape, label)
# help(train_data)

# torch的图像格式： NCHW(图像数量，通道，高度，宽度)
# 保存图像torch的顺序与opencv不同
for i in  range(10):
    # 取图像
    image, label = valid_data[i]#此处image为一个张量
    # 转换为opencv
    # 1. 转为numpy
    image = image.cpu().clone().numpy()#image不再是张量一定在cpu上才能用numpy
    # 2. 转为0-255
    image = image * 255
    # 3. 取整
    image = image.astype(numpy.uint8)
    # 4. 通道转为第三维
    image = image.transpose([1, 2, 0])#(高度，宽度，通道)
    # 5. 保存
    cv2.imwrite(F"img_{i}_{label}.png", image)

# 2. 转换为批次数据集
train_loader = DataLoader(train_data, batch_size=10, shuffle=True)
                #batch_size批次大小(一个批次10张图) shuffle是否需要打乱
# DataLoader : __iter__
for images, labels in train_loader:
    print(images.shape)
    print(labels)
    break
