#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


df = pd.read_csv('dataset_Facebook.csv', delimiter=';')


# In[6]:


df.head()


# In[8]:


df.columns


# In[15]:


subset1 = df[['Type','Paid','Page total likes']]
subset1


# In[23]:


subset2 = df[['Type','Lifetime Post Consumers','Lifetime Engaged Users']]
subset2


# In[24]:


merged_data = pd.merge(subset2, subset1)
merged_data


# In[28]:


sorting = merged_data.sort_values(by=['Paid'], ascending = False)
sorting


# 

# In[30]:


merged_data.transpose()


# In[31]:


df.shape


# In[32]:


test1 = df.iloc[[1,2,3,4,5],[15,16,17]]
test1


# In[33]:


test2 = test1.melt(id_vars='comment', value_vars=['like', 'share'])
test2


# In[ ]:




