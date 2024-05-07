#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('airquality_data.csv', encoding='cp1252')


# In[3]:


df.head()


# In[4]:


df.info


# In[5]:


df.columns


# In[6]:


df.dtypes


# In[7]:


df['so2'] = df['so2'].astype('float32')
df['no2'] = df['no2'].astype('float32')
df['rspm'] = df['rspm'].astype('float32')
df['spm']  = df['spm'].astype('float32')
df['pm2_5'] = df['pm2_5'].astype('string')


# In[8]:


df.dtypes


# In[9]:


df = df.drop_duplicates()


# In[10]:


df.isna().sum()


# In[11]:


percent_missing = df.isnull().sum()*100/len(df)


# In[12]:


percent_missing.sort_values(ascending=False)


# In[13]:


df=df.drop(['stn_code', 'agency','sampling_date','location_monitoring_station','pm2_5'], axis = 1) 


# In[14]:


df.columns


# In[15]:


#data integration
subset_1 = df[['state', 'location']]
subset_1


# In[16]:


subset_2 = df[['state','type']]
subset_2


# In[19]:


concatenated_df =pd.concat([subset_1,subset_2],axis=1)
concatenated_df


# In[20]:


#Error Correcting
def remove_outliers(column): 
    Q1=column.quantile(0.25)
    Q3=column.quantile(0.75)
    IQR  = Q3 - Q1
    threshold = 1.5*IQR
    outliers_mask = (column < Q1 - threshold) | (column > Q3 - threshold)
    return column[~outliers_mask]


# In[21]:


col_name = ['so2', 'no2', 'rspm', 'spm']
for col in col_name:
  df[col] = remove_outliers(df[col])


# In[22]:


#Data Transform
from sklearn.preprocessing import LabelEncoder

col_label= ['state','location','type']
# Initialize LabelEncoder

encoder = LabelEncoder()
# Iterate over columns
for col in df.columns:
        # Fit and transform the column
        df[col] = encoder.fit_transform(df[col])


# In[23]:


df


# In[ ]:




