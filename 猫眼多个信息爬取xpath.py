#!/usr/bin/env python
# coding: utf-8

# In[20]:


import requests
from lxml import etree

url = 'https://maoyan.com/films/1203'
data = requests.get(url).text
s=etree.HTML(data)

film=s.xpath('normalize-space(/html/body/div[3]/div/div[2]/div[1]/h3/text())')
director=s.xpath('normalize-space(//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li/div/a/text())')
actor=s.xpath('normalize-space(//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div/div[2]/ul/li[1]/div/a[1]/text())')
time=s.xpath('normalize-space(/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text())')

print('电影名称：',film)
print('导演：',director)
print('主演：',actor)
print('片长：',time)


# In[ ]:




