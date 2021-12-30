import torch
from torch.nn import CrossEntropyLoss   # 可调用对象(损失函数)
from torch.optim import Adam        # 优化器用途：更新w,b
from lenet5 import Lenet5
from datasets import load_mnist
import os

# 获取模块的安装路径
current_dir = os.path.dirname(__file__)

class Lenet5Trainer:

    def __init__(self, epoch, lr):
        super(Lenet5Trainer, self).__init__()
        # 判定是否支持GPU
        self.CUDA = torch.cuda.is_available()
        # 模型参数(用于保存模型xxx.pt)路径可能改变
        self.mod_file = os.path.join(current_dir, "mods/lenet5.pt")#(当前路径，文件中的相对路径)
        # 1. 准备数据集
        self.train_loader, self.valid_loader = load_mnist(batch_size=1000)#批次数据集 数据集打乱测试集不打乱
        # 2. 准备模型
        self.net = Lenet5()
        if self.CUDA:
            self.net = self.net.cuda()
        # -----------------
        if os.path.exists(self.mod_file):#判定是否存在模型
            print("加载已有模型")
            state_dict = torch.load(self.mod_file)  # 加载到缓冲
            self.net.load_state_dict(state_dict)    # 加载到模型
        else:
            print("从新训练")
        # -----------------
        # 3. 超参数 lr学习率 epoch训练次数
        self.lr = lr 
        self.epoch= epoch
        # 4. 准备训练对象：优化器。损失函数
        self.optimizer = Adam(self.net.parameters(), lr=self.lr)#更新传递参数
        self.loss_f = CrossEntropyLoss()#损失函数
    
    def train_one(self):
        # 批循环训练
        for x, y in self.train_loader:#一个批次一个批次的训练
            if self.CUDA:
                x = x.cuda()
                y = y.cuda()
            # 预测
            y_ = self.net(x)
            # 计算损失值
            loss = self.loss_f(y_, y)
            # 求导
            loss.backward()
            # 使用优化器更新权重参数
            self.optimizer.step()
            # 导数清空
            self.optimizer.zero_grad()   
            # print(F"\t损失:{loss:8.6f}")  #8位数，6位小数

    def train(self):
        print("开始训练")
        for e in  range(self.epoch):
            print(F"第{e:03d}轮训练")
            self.train_one()#训练
            # ----------------------保存模型
            # 获取所有的权重系数的字典
            state_dict = self.net.state_dict()
            torch.save(state_dict, self.mod_file)
            # ----------------------
            self.valid()#验证
            #保存模型
            
    
    @torch.no_grad()#保证其中运算不会被自动求导所跟踪
    def valid(self):
        v_loss = 0.0       #累加损失值
        v_correct_num = 0.0#正确数量
        v_total_num = 0    #样本数
        for vx, vy in self.valid_loader:
            if self.CUDA:
                vx = vx.cuda()
                vy = vy.cuda()
            # 累加预测样本数
            v_total_num += len(vx)
            # 预测
            vy_ = self.net(vx)
            # 计算为概率
            prob = torch.softmax(vy_, dim=1)
            # 取出最大下标（预测结果）
            pred_y = torch.argmax(prob, dim=1)
            # 用预测结果与实际标签对比，计算正确率
            v_correct_num += (vy == pred_y).float().sum()#逻辑变量vy==pred_y转成浮点数(1.0 0.0)再求和
            # 累加损失值
            v_loss += self.loss_f(vy_, vy)
        print(F"\t损失值：{v_loss:8.6f},正确率：{v_correct_num/v_total_num * 100: 6.2f}")



if __name__ == "__main__":
    trainer = Lenet5Trainer(epoch=10, lr=0.0001)#参数放在构造器里
    trainer.train()

