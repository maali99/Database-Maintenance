#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import os
import datetime as dt
import numpy as np


# In[2]:


test = [x for x in os.listdir("/Users/Ahmad/Documents") if x.endswith(".txt")]
print(test)
len(test)


# In[3]:


master=[]
for i in range(0,len(test)):
    temp=test[i]
    slave=[temp[0:8]]
    master+=slave
print(master)


# In[4]:


current_date=dt.datetime.today()
d=current_date.strftime('%Y%m%d')


# In[5]:


d


# In[6]:


for i in range(0,len(test)):
    if int(d)-7>int(master[i]):
        os.remove("/Users/Ahmad/Documents/" + test[i])
        print("File deleted")
    else:
        print("File not older than 7 days")


# In[ ]:




