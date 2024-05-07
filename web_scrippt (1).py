#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import bs4


# In[4]:


req = requests.get('https://www.etsy.com/ca/listing/1375008231/aluminum-composite-panel-dibond-acp-3mm?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=aluminum&ref=sc_gallery-1-1&sts=1&plkey=f196afa4b937468dcc195bf9bb59b383262c3236%3A1375008231')


# In[5]:


req


# In[6]:


req.content


# In[9]:


Soup = bs4.BeautifulSoup(req.text)
Soup


# In[11]:


reviews = Soup.findAll('div',{'class':'wt-content-toggle--truncated-inline-multi wt-break-word wt-text-body'})
for review in reviews:
    print(review.get_text()+'\n\n')


# In[19]:


rating = Soup.find('span',{'class':'wt-display-inline-block wt-mr-xs-1'}).get_text();
print(rating)


# In[23]:


individual_rating = Soup.findAll('span',{'class':'wt-screen-reader-only'})
for indiv_rating in individual_rating:
    print(indiv_rating.get_text()+'\n')


# In[35]:


Customer = Soup.findAll('a',{'class':"wt-text-link wt-mr-xs-1"})
for cust in Customer:
    print(cust.get_text()+'\n')


# In[ ]:





# In[ ]:




