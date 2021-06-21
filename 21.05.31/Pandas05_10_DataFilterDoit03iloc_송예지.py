
# coding: utf-8

# ### iloc 속성으로 행 데이터 추출하기(p37)

# In[1]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')
df


# In[2]:


df.head(3)


# In[3]:


df.iloc[1]


# In[4]:


df.iloc[99]


# In[5]:


df.iloc[-1]


# In[6]:


print(df.tail(1))
print()
print(df.shape)
print()
print(df.iloc[1703])


# In[7]:


print(df.iloc[[0,99,999]])

