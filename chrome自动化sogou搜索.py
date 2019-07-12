#!/usr/bin/env python
# coding: utf-8

# In[34]:



 
from selenium import webdriver
import time
 
 
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
#上面两条解决: 
#chrome浏览出现黄色的提示 "您使用的是不受支持的命令行标记:--ignore-certificate-errors.稳定性和安全性会有所下降"
 
 
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.sogou.com/")   #打开浏览器并访问URL地址
 
 
driver.find_element_by_id("query").clear()       #clear()清除        
#通过id=kw定位搜索框界面元素,在调用clear()方法来清除搜索框内容
 
 
driver.find_element_by_id("query").send_keys("ariel a")  #send_keys() 发送关键字
#自动输入linuxhub进行搜索
 
 
driver.find_element_by_id("stb").click()   # click()点击
#通过id=su定位搜索按钮,并通过click()方法进行提交搜索
 
 
print (driver.title)  #当前浏览器页面中的title
 


# In[4]:





# In[ ]:




