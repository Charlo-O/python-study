#!/usr/bin/env python
# coding: utf-8

# # 第三次课作业

# ## （1）Pandas基础知识

# （1）用字典数据类型创建DataFrame。
# data={'state':['a','b','c','d'],
# 'year':[1991,1992,1993,1994],
# 'pop':[6,7,8,9]}

# In[2]:


import pandas as pd 
data={'state':['a','b','c','d'], 'year':[1991,1992,1993,1994], 'pop':[6,7,8,9]}
df=pd.DataFrame(data)
df


# （2）将创建的Dataframe的索引设置为，ABCD。并且命名为“索引”。

# In[3]:


df.index=['A','B','C','D']
df.index.name='索引'
df


# （3）在下面新增一行。然后删除。

# In[7]:


s=pd.Series({'state':'e','year':1995,'pop':10})
s.name='E'


# In[8]:


df=df.append(s)
df


# In[9]:


df=df.drop(['E'])# 删除后的视图
df


# （4）增加新的属性列，列名设置为‘port’，值均为1。

# In[11]:


df['port']=1,2,3,4


# In[12]:


df


# In[ ]:





# （5）取出1991和1994年的数据。

# In[35]:


df.loc[['A','D']]  # 取行加 .loc


# In[34]:


df


# （6）获取前‘state’和‘year’的数据。

# In[19]:


df[['state','year']]


# （7）查看每一列数据的数据格式，并且将‘pop’每个数据乘2。

# In[30]:


df.dtypes


# In[31]:





# In[36]:


data={'state':['a','b','c','d'], 'year':[1991,1992,1993,1994], 'pop':[6,7,8,9]}
df=pd.DataFrame(data)
df


# In[37]:


df.index=['A','B','C','D']
df.index.name='索引'
df


# In[38]:


s=pd.Series({'state':'e','year':1995,'pop':10})
s.name='E'
df=df.append(s)
df


# In[39]:


df['pop']=df['pop']*2
df


# In[42]:


df['port']=1,2,3,4,5
df


# In[45]:


df.drop(['port'],axis=1) # 列为行 0 为列


# In[ ]:


df.drop(['port'],axis=1，implace=true) # 1为行 0 为列  操作结果


# ## （2）数据操作

# （1）读取香港酒店数据。

# In[1]:


import pandas as pd
df=pd.read_excel('C:/Users/Charlo/Desktop/python 习题/香港酒店数据.xlsx')


# In[3]:


df[:5]


# In[14]:


df=df[1:]


# In[15]:


df


# In[16]:


df[:5]


# In[17]:


df.index=range(0,len(df))
df[:5]


# In[20]:


df.columns=['序号','名字','类型','城市','地区','地点','评分','评分人数','价格']


# In[21]:


df[:5]


# （2）按照数据的内容，重新设置数据的索引，重新设置列名称为'名字','类型','城市','地区','地点','评分','评分人数','价格'。

# （3）查看所有类型为“浪漫情侣”的酒店

# In[25]:


df[df.类型=='浪漫情侣']


# （4）查看所有类型为“浪漫情侣”，地区在湾仔的酒店

# In[27]:


df[(df.类型=='浪漫情侣')&(df.地区=='湾仔')]


# （5）查看所有地址在观塘或者油尖旺，评分大于4的酒店

# In[29]:


df[(df.地区=='观塘')|(df.地区=='油尖旺')&(df.评分>4)]


# （6）查看类型缺失的数据

# In[35]:


df[df['类型'].isnull()]


# In[36]:


df[df['类型'].notnull()]


# （7）用“其他”填充类型和地区

# In[38]:


df['类型'].fillna('其他类型',inplace=True)
df['地区'].fillna('其他地区',inplace=True)


# In[40]:


df[df['类型'].isnull()]


# （8）用评分均值填充缺失值

# In[42]:


df['评分'].fillna(df['评分'].mean(),inplace=True)


# （9）删除价格和评分人数的缺失值

# In[44]:


df[df['价格'].isnull()]


# In[45]:


df[df['评分人数'].isnull()]


# In[46]:


df.dropna(inplace=True)


# In[54]:


df.drop(['序号'],axis=1,inplace=True)


# In[56]:


df.index=range(0,len(df))


# In[57]:


df


# （10）保存到“酒店数据1.xlsx”

# In[60]:


df.to_excel('酒店数据1.xlsx')


# In[ ]:




