#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/python
# coding: utf-8

import requests
link = "http://www.charlo.cn/"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'} 
r = requests.get(link, headers= headers)

print (r.text)


# In[ ]:




