
# coding: utf-8

# In[14]:


import numpy as np

# python list 中可以存储多种数据类型 所以处理速度慢
lst = [[1,3,5,], [2,4,6]]
print(type(lst))

# numpy 的 array 中只可以存储一种数据类型 
np_lst = np.array(lst)
print(type(np_lst))

np_lst = np.array(lst, dtype=np.float)
# bool, int, int8~128, uint8~128, float, string
print(np_lst.shape)
print(np_lst.ndim) # 维度
print(np_lst.dtype)
print(np_lst.itemsize) # 每个元素的大小 64位占8个字节
print(np_lst.size) # 一共6个元素

# 常用数组
print(np.zeros([2,4]))
print(np.ones([3, 5]))

# 随机数
print(np.random.rand(2, 4))
print(np.random.rand())
print(np.random.randint(1,10,3))
print(np.random.randn(2, 4)) # 标准正态分布的随机数
print(np.random.choice([10, 20, 30], 2))
print(np.random.beta(1,10,10)) # beta 分布


# 数组操作
print("*****************数组操作******************")
print(np.arange(1, 11)) # 等差数列
print(np.arange(1, 11).reshape([2, 5])) 
print(np.arange(1, 11).reshape([2, -1]))  # -1表示缺省

print("*****************")
lst = np.arange(1, 11).reshape([2, -1])
print(np.exp(lst)) # 指数
print(np.exp2(lst))
print(np.sqrt(lst))
print(np.sin(lst))
print(np.log(lst))

print("*****************")
lst = np.array([[[1,2,3,4], 
                [4,5,6,7]], 
                [[7,8,9,10], 
                [10,11,12,13]],
                [[14,15,16,17],
                [18,19,20,21]]])
print(lst.sum())
print("")
print(lst.sum(axis=0)) # max(axis) = 维数-1
print("")
print(lst.sum(axis=1)) # 
print("")
print(lst.sum(axis=2))

print("*****************")
print(lst.max())
print("")
print(lst.max(axis = 0))
print("")
print(lst.max(axis = 1))
print("")
print(lst.max(axis = 2))
# 类似函数还有 min()

print("*****************")
lst1 = np.array([10, 20, 30, 40])
lst2 = np.array([4, 3, 2, 1])
print(lst1 + lst2)
print(lst1 - lst2)
print(lst1 * lst2)
print(lst1 / lst2)
print(lst1 ** lst2)

print("*****************")
print(np.dot(lst1, lst2))
print(np.dot(lst1.reshape([2,2]), lst2.reshape([2,2])))

print("*****************")
print(np.concatenate((lst1, lst2), axis = 0))
print(np.vstack((lst1, lst2)))
print(np.hstack((lst1, lst2)))
print(np.split(lst1, 2))

print("*****************")
from numpy.linalg import *

print(np.eye(3)) # 单位矩阵

lst = np.array([[1., 2.], [3., 4.]])
print(inv(lst)) # 矩阵的逆
print(lst.transpose()) # 矩阵的转置
print(det(lst)) # 行列式
print(eig(lst)) # 特征值 特征向量

y = np.array([[5.], [7.]])
print(solve(lst, y)) # 解方程 -3 * 1 + 2 * 4 = 5

print("*****************")





