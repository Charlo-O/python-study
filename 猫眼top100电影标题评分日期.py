#!/usr/bin/env python
# coding: utf-8

# In[60]:


from lxml import etree
import requests
import time
for a in range(10):
    url = 'https://maoyan.com/board/4?start={}'.format(a*10)
    data = requests.get(url).text
    
    s=etree.HTML(data)
    file=s.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    time.sleep(3)

    for div in file:
        title = div.xpath("./div/div/div[1]/p[1]/a/@title")[0]
        score1=div.xpath('./div/div/div[2]/p/i[1]/text()')[0]
        score2=div.xpath('./div/div/div[2]/p/i[2]/text()')[0]
        num=div.xpath('./div/div/div[1]/p[3]/text()')[0]
        
        print("{},{}{},{}\n".format(title,score1,score2,num)) 


# In[ ]:





# In[52]:


(/*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1])
(/*[@id="content"]/div/div[1]/ol/li[1]/div)


# In[ ]:




