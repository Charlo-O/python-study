#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from lxml import etree
import requests
import time
for a in range(10):
    url = 'https://movie.douban.com/top250?start={}'.format(a*25)
    data = requests.get(url).text
    
    s=etree.HTML(data)
    file=s.xpath('//ol[@class="grid_view"]/li')
    time.sleep(3)

    for div in file:
        title =div.xpath('.//span[@class="title"]/text()')[0]
        score=div.xpath('.//span[@class="rating_num"]/text()')[0]
        num=div.xpath('.//div[@class="star"]/span/text()')[1]
        

        
        print("{},{},{}\n".format(title,score,num)) 


# In[ ]:





# In[ ]:


(/*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1])
(/*[@id="content"]/div/div[1]/ol/li[1]/div)

