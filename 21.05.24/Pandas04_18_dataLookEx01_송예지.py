
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv('./../data/gapminder.tsv',sep='\t')
print(df)


# In[4]:


type(df)


# In[5]:


print(df.columns)


# In[6]:


df.index


# In[7]:


print(df.dtypes)


# In[10]:


print(df.info())


# In[9]:


df.shape

