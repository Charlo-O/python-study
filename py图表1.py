#!/usr/bin/env python
# coding: utf-8

# # 第六次课作业

# （1）画出$y=x^{2}+2x+1$在区间[-5,3]的函数图像。

# In[3]:


get_ipython().run_line_magic('pylab', 'inline')
# 可视数据
import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif']=['SimHei'] # 中文字体 黑体
plt.rcParams['axes.unicode_minus']=False    #正常显示负号


# In[6]:


x=np.linspace(-5,3,200)
y=x**2+2*x+1


# In[8]:


y


# In[23]:


plt.figure(figsize(9,6))
x=np.linspace(-5,3,200)
y=x**2+2*x+1
plt.plot(x,y,'r-') # r- r 为红色 -为实线 - -虚线 

plt.plot([-1,-1],[0,16],'b-') #对称轴

plt.xlabel('X轴',fontsize=20)
plt.ylabel('Y轴',fontsize=20)
plt.title('y=x**2+2*x+1',fontsize=20)
plt.show()


# （2）在同一张图中创建两个子图，分别画出sinx和cosx在[-3.14,3.14]上的函数图像。设置线条宽度为2.5.

# In[37]:


x=np.linspace(-3.14,3.14,200)
y1=np.sin(x)
y2=np.cos(x)

plt.figure(figsize(20,20))
plt.subplot(211)  #创建两行一列的画布，第一个的图像 全称plt.subplot(2，1，1)

plt.xlabel('X轴',fontsize=20)
plt.plot(x,y1,'r-',x[::20],y1[::20],'k+',linewidth=2.5) #x[::20],y1[::20],'k+' 每隔20点加加号点标记      

plt.subplot(212)
plt.xlabel('X轴',fontsize=20)
plt.plot(x,y2,'b-',linewidth=2.5)

plt.show()


# （3）读取上次作业保存的酒店数据，画出每个地区酒店数量的柱状图，柱状颜色为红色

# In[6]:


df=pd.read_excel('C:/Users/Charlo/Desktop/酒店数据2.xlsx')


# In[36]:


df[:5]


# In[37]:


df['地区'].unique()


# In[7]:


data=df['地区'].value_counts() 


# In[41]:


data


# In[8]:


data=df['地区'].value_counts()


# In[43]:


data.index


# In[44]:


data.values


# In[11]:


data=df['地区'].value_counts()
x=data.index
y=data.values

plt.figure(figsize=(10,6))
plt.bar(x,y,color='r')
plt.title('各地区酒店数量',fontsize=20)
plt.xlabel('地区',fontsize=16)
plt.ylabel('酒店数量',fontsize=20)
plt.tick_params(labelsize=18)
plt.xticks(rotation=45)
for a,b in zip(x,y):
    plt.text(a,b+1,'%.0f' % b, ha='center',va='bottom',fontsize=10)

plt.show() 


# （4）画出每个价格等级酒店数量的柱状图。

# In[54]:


data=df['等级'].value_counts()
x=data.index
y=data.values


# In[51]:


y


# In[55]:


x


# In[9]:


data=df['等级'].value_counts()
x=data.index
y=data.values

plt.figure(figsize=(10,6))
plt.bar(x,y,color='b')
plt.title('价格等级酒店数量',fontsize=20)
plt.xlabel('价格等级',fontsize=16)
plt.ylabel('酒店数量',fontsize=20)
plt.tick_params(labelsize=18)

for a,b in zip(x,y):
    plt.text(a,b+1,'%.0f' % b, ha='center',va='bottom',fontsize=10)

plt.show() 


# In[ ]:





# （5）画出各个价格等级占比的饼图。

# In[61]:


data=df['等级'].value_counts()


# In[68]:


data


# In[12]:


data=df['等级'].value_counts()
label=data.index
y=data.values
y=y/sum(y) #占比


# In[13]:


y


# In[16]:


data=df['等级'].value_counts()
label=data.index
y=data.values
y=y/sum(y) #占比

plt.figure(figsize=(10,6))
plt.title('价格等级占比',fontsize=20)

# 生成数据
#labels = ['A', 'B', 'C', 'D', '其他']
#share = [0.45, 0.25, 0.15, 0.05, 0.10]



# 分裂饼图
plt.pie(y, 
        labels = label, autopct = '%3.1f%%',
        startangle = 180, shadow = True,
        colors = ['c', 'r',  'y'])

    
plt.legend()
plt.show()


# （6）画出酒店评分的直方图。

# In[25]:


data=df['评分'].value_counts()


# In[30]:


plt.figure(figsize=(10,6))
plt.hist(df['评分'],bins=20
         ,color='r')

plt.title('酒店评分的分布图',fontsize=20)
plt.xlabel('分数',fontsize=16)
plt.ylabel('数量',fontsize=20)
plt.tick_params(labelsize=15)
plt.show()


# （7）画出每个热门等级酒店评分均值的柱状图。（按照评分均值从小到大排序。）

# In[32]:


data=df['评分'].groupby(df['等级']).mean()


# In[33]:


data=data.sort_values()


# In[34]:


data


# In[35]:


x=data.index
y=data.values

plt.figure(figsize=(10,6))
plt.bar(x,y,color='b')

plt.title('各热门等级平均分',fontsize=20)
plt.xlabel('热门等级',fontsize=16)
plt.ylabel('平均得分',fontsize=20)
plt.tick_params(labelsize=18)

for a,b in zip(x,y):
    plt.text(a,b+0.01,'%.2f' % b, ha='center',va='bottom',fontsize=10)
plt.show()


# In[ ]:




