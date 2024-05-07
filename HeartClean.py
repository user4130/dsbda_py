#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# In[2]:


df = pd.read_csv("Heart.csv")
df.head()


# In[3]:


df = df.drop_duplicates()


# In[4]:


df.describe()


# In[5]:


df.info()


# In[6]:


df.isna().sum()


# In[7]:


#Data Integration
df.head()


# In[8]:


df.fbs.unique()


# In[9]:


subSet1 = df[['age','cp','chol','thalach']]


# In[10]:


subSet2 = df[['exang','slope','target']]


# In[11]:


merging = subSet1.merge(right=subSet2,how='cross')
merging.head()


# In[12]:


#Error Correcting
df.columns


# In[13]:


def remove_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    threshold = 1.5 * IQR
    outlier_mask = (column < Q1 - threshold) | (column > Q3 + threshold)
    return column[~outlier_mask]


# In[14]:


col_name = ['cp','thalach','exang','oldpeak','slope','ca']
for col in col_name:
    df[col] = remove_outliers(df[col])


# In[22]:


plt.figure(figsize=(10, 6))
for col in col_name:
    sns.boxplot(data=df[col])
    plt.title(col)
    plt.show()


# In[38]:


from sklearn.preprocessing import StandardScaler


# In[39]:


scaler = StandardScaler()


# In[40]:


x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


# In[41]:


#Data model building


# In[42]:


y_train= np.array(y_train).reshape(-1, 1)
y_test= np.array(y_test).reshape(-1, 1)


# In[43]:


y_train.shape


# In[47]:


model = LogisticRegression()
model.fit(x_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(x_test_scaled)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# In[ ]:




