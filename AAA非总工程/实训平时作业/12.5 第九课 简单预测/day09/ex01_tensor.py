import torch
import numpy
# 创建张量
# 1. 构造器
# IntegerTensor/LongTensor/DoubleTensor
# FloatTensor = Tensor
# t = torch.FloatTensor([1.0])  #只能FloatTensor才能求导
t = torch.Tensor(numpy.array([1.0]))  # 把标量数组，向量就可以直接转换为张量
print(t)
# 2. 函数
t = torch.tensor([1.0], dtype=torch.float)
print(t)
# 3. from_numpy
t = torch.from_numpy(numpy.array(
    [
        [1.0, 2.0, 3.0],
        [1.0, 2.0, 3.0],
        [1.0, 2.0, 3.0]
    ]
))
print(t)
# 操作张量 (所有向量的操作都支持)
# 1. shape
print(t.shape)
# 2. 下标运算与向量一样
print(t[1])
print(t[1, 1])
print(t[0:2, 1:3])
s = t>2
print(t[s])
# Tensor/ndarray/list(tuple)
n = t.numpy()
print(n)

# gpu与cpu运算
# ct = t.cpu()
gt = t.cuda()
print(gt)

# 为了防止数据共享一个内存:copy
w = t.clone()
print(w)

# 张量处在一个求导的上下文图跟踪，为了 让张量不被求导运算跟踪，剥离张量的环境
v=t.detach().numpy()
print(v)
