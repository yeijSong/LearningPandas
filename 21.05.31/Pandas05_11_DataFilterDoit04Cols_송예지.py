
# coding: utf-8

# ### 데이터 추출하기-슬라이싱 구문,range메서드(p39)

# #### 1. 슬라이싱 구문으로 데이터 추출하기

# In[1]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')
df


# In[2]:


df.head(3)


# In[3]:


subset=df.loc[:,['year','pop']]
print(subset.head())


# In[4]:


subset=df.iloc[:,[2,4,-1]]
print(subset.head())

