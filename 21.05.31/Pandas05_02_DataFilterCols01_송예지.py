
# coding: utf-8

# In[2]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[3]:


country_df=df['country']

print(type(country_df))


# In[4]:


print(country_df.head())


# In[5]:


print(country_df.tail())


# In[7]:


subset=df[['country','continent','year']]

print(type(subset))


# In[8]:


print(subset.head())


# In[9]:


print(subset.tail())

