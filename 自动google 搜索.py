#!/usr/bin/env python
# coding: utf-8

# In[24]:


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

input = driver.find_element_by_name('q')
input.send_keys("ariel a")


button  = 'document.getElementsByClassName("gNO89b")[0].click();'
driver.execute_script(button )


# In[ ]:




