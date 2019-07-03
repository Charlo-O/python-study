#!/usr/bin/env python
# coding: utf-8

# In[38]:


# 先导入我们需要的库
import requests
import re
from bs4 import BeautifulSoup
#发送“请求”
kv = {'User-Agent': 'Mozilla/5.0'}
r = requests.get('https://book.douban.com/top250?icn=index-book250-all', headers = kv)
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')


# 从解析文件中通过select选择器定位指定的元素，返回一个列表
titles = soup.select('div.pl2 > a ')
# 对返回的列表进行遍历
for i in titles:
    
    title = i.get_text()
       
    print(title) 
        


# In[ ]:





# In[ ]:




