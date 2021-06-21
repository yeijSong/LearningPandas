
# coding: utf-8

# ### 데이터 추출하기-슬라이싱 구문,range메서드(p39)

# #### 2. range 메서드로 원하는 데이터 추출하기

# In[1]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')
df


# In[2]:


small_range=list(range(5))
print(small_range)


# In[3]:


df.head(3)


# In[4]:


subset=df.iloc[:,small_range]
print(subset.head())


# In[6]:


small_range2=list(range(3,6))
print(small_range2)


# In[7]:


subset2=df.iloc[:,small_range2]
print(subset2.head())


# In[8]:


small_range3=list(range(0,6,2))
print(small_range3)


# In[9]:


subset3=df.iloc[:,small_range3]
print(subset3.head())

