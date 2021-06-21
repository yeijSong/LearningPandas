
# coding: utf-8

# In[1]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[2]:


df.head(3)


# In[3]:


df.shape


# In[4]:


loc00=df.loc[0]
loc00


# In[5]:


type(loc00)


# In[6]:


df.loc[90:100]


# In[7]:


df.loc[99]


# In[8]:


df.tail(3)


# In[9]:


df.loc[-1] # -1과 같이 인덱스에 없는 값을 사용하면 오류가 발생


# In[10]:


len(df)

