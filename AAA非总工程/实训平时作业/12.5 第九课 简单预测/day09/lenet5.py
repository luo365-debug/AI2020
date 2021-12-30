import torch
from torch.nn import Module
from torch.nn import Conv2d, Linear#卷积运算conv2d，线性运算linear
from torch.nn.functional import max_pool2d, relu  #磁化函数 激活函数(<0忽略)
from datasets import load_mnist

class Lenet5(Module):

    def __init__(self):
        super(Lenet5, self).__init__()
        # 定义有参数运算，主要目的就是初始化参数，设置为可求导
        #一张图像变六个卷积核
        self.conv1 = Conv2d(in_channels= 1, out_channels=  6, kernel_size=5, stride=1, padding=2)
        #6个卷积核变成16个卷积特征
        self.conv2 = Conv2d(in_channels= 6, out_channels= 16, kernel_size=5, stride=1, padding=0)
        #16变120个特征图
        self.conv3 = Conv2d(in_channels=16, out_channels=120, kernel_size=5, stride=1, padding=0)

        self.fc1 = Linear(120, 84)
        self.fc2 = Linear(84, 10) 


    def forward(self, x):
        # 定义运算过程
        y = x
        # ---------------1第一层卷积运算 1 * 1 * 28 * 28
        y = self.conv1(y)  # self.conv1.forward(y) # 可调用对象
        y = max_pool2d(y, (2, 2))   #降维(?)
        y = relu(y, inplace=True)  # -的像素变成0：激活函数
        # ---------------2 1 * 6 * 14 * 14
        y = self.conv2(y)
        y = max_pool2d(y, (2, 2))
        y = relu(y, inplace=True)
        # ---------------3  1 * 16 * 5 *5
        y = self.conv3(y)
            #1*1无法磁化
        y = relu(y, inplace=True)   # 1 * 120 * 1 * 1

        # 格式转换
        y = y.view(-1, 120)
        # --------------4
        y = self.fc1(y)
        y = relu(y, inplace=True)
        # --------------5
        y = self.fc2(y)  # 最后不需要激活
        return y


net = Lenet5()
train, valid = load_mnist(batch_size=10)
for x, y in train:
    print("输入的形状：",x.shape)
    y_ = net(x)  # 预测值
    print("输出的形状：",y_.shape)
    # 转换为概率
    prob = torch.softmax(y_, dim=1)
    print(prob.detach().numpy())
    # 预测哪个数字
    cls_idx = torch.argmax(prob, dim=1)
    print(cls_idx.numpy()) #找到概率最大的数
    break
# 怎么训练？
