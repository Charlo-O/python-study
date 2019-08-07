#!/usr/bin/env python
# coding: utf-8

# # 第二次课作业

# （1）创建一个1到10的数组，然后逆序输出。

# In[1]:


import numpy as np
from numpy import *
a=np.array([1,2,3,4,5,6,7,8,9,10])
a[::-1]


# In[7]:


a=np.arange(1,11)
a[::-1]


# （2）创建一个长度为20的全1数组，然后变成一个4×5的二维矩阵并转置。

# In[10]:


a=np.ones(20,dtype='int')
a


# In[11]:


a.shape


# In[13]:


b=a.reshape(4,5)
b


# In[14]:


a


# In[15]:


b.T


# （3）创建一个3x3x3的随机数组。
# (提示: np.random.random)

# In[21]:


a=np.random.random((3,3,3))
a


# （4）从1到10中随机选取10个数，构成一个长度为10的数组，并将其排序。获取其最大值最小值，求和，求方差。

# In[23]:


a=np.random.randint(1,11,10) #左闭右开
a


# In[25]:


a.sort()
a


# In[26]:


a.max()


# In[29]:


a.sum()


# In[31]:


a.var() #方差


# （5）从1到10中随机选取10个数，构成一个长度为10的数组，选出其中的奇数。

# In[33]:


a=np.random.randint(1,11,10)
a


# In[34]:


a[where(a%2==1)]


# （6）生成0到100，差为5的一个等差数列，然后将数据类型转化为整数。

# In[36]:


a=np.linspace(0,100,21)
a


# In[37]:


a.astype('int32')


# （7）从1到10中随机选取10个数，大于3和小于8的取负数。

# In[38]:


a=np.random.randint(1,11,10)
a


# In[39]:


a[(a>3)&(a<8)]*=-1
a


# （8）在数组[1, 2, 3, 4, 5]中相邻两个数字中间插入1个0。

# In[40]:


a=[1,2,3,4,5]
b=np.zeros(9,dtype='int')
b[::2]=a
b


# （9）新建一个5乘5的随机二位数组，交换其中两行？比如交换第一二行。

# In[50]:


a=np.random.randint(1,10,(5,6))
a


# In[42]:


a[0]


# In[44]:


a[:,1]


# In[52]:


a=a[[1,0,2,3,4]]


# In[53]:


a


# （10）把一个10\*2的随机生成的笛卡尔坐标转换成极坐标。

# In[54]:


a=np.random.randint(1,10,(10,2))
x=a[:,0]
y=a[:,1]


# In[56]:


x=a[:,0]
y=a[:,1]


# In[57]:


r=np.sqrt(x**2+y**2)
r


# In[58]:


R=np.arctan(y/x)
R


# In[ ]:





# （11）创建一个长度为10并且除了第五个值为1其余的值为2的向量。

# In[2]:


a=np.ones(10,dtype='int')*2
a[4]=1
a


# In[ ]:





# （12）创建一个长度为10的随机向量，并求其累计和。

# In[5]:


a=np.random.randint(1,10,10)
a


# In[7]:


a.cumsum()


# （13）将数组中的所有奇数替换成-1。

# In[9]:


a=np.random.randint(1,10,10)
a[a%2==1]=-1


# In[10]:


a


# （14）构造两个4乘3的二维数组，按照3种方法进行连接？

# In[33]:


a=np.random.randint(1,10,(4,3))
b=np.random.randint(1,10,(4,3))


# In[34]:


a


# In[35]:


b


# In[36]:


vstack((a,b))


# In[37]:


dstack((a,b))


# In[38]:


hstack((a,b))


# In[ ]:





# （15）获取数组 a 和 b 中的共同项（索引位置相同，值也相同）。
# a = np.array([1,2,3,2,3,4,3,4,5,6])，b = np.array([7,2,10,2,7,4,9,4,9,8])

# In[25]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c=a-b
c


# In[26]:


where(c==0)


# （16）从数组 a 中提取 5 和 10 之间的所有项。a=np.array([7,2,10,2,7,4,9,4,9,8])

# In[27]:


a=np.array([7,2,10,2,7,4,9,4,9,8])
a[(a>5)&(a<10)]


# In[ ]:




