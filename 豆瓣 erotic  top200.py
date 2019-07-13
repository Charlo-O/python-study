#!/usr/bin/env python
# coding: utf-8

# In[25]:


import requests
import json
import time
with open('C:/Users/Charlo/Desktop/erotic.csv','w',encoding='utf-8') as f:

    for a in range(10):
        url_visit = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}&genres=%E6%83%85%E8%89%B2'.format(a*20)
        file = requests.get(url_visit).json()   #这里跟之前的不一样，因为返回的是 json 文件
        time.sleep(2)

        for i in range(20):
            dict=file['data'][i]   #取出字典中 'data' 下第 [i] 部电影的信息
            urlname=dict['url']
            title=dict['title']
            rate=dict['rate']
            cast=dict['casts']

            f.write('{},{},{},{}\n'.format(title,rate,'  '.join(cast),urlname))


# In[ ]:





# In[ ]:




