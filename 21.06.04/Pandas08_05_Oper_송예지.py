
# coding: utf-8

# ## 벡터와 스칼라로 브로드캐스팅 수행하기(p61)
# * 브로드캐스팅(Broadcasting) : 시리즈나 데이터프레임에 있는 모든 데이터에 대해 한 번에 연산하는 것
# * 벡터 : 시리즈처럼 여러 개의 값을 가진 데이터
# * 스칼라 : 단순 크기를 나타내는 데이터

# In[2]:


import pandas as pd

scientists=pd.read_csv('./../data/scientists.csv')
scientists


# In[3]:


ages=scientists['Age']
ages


# In[4]:


ages+ages


# In[5]:


ages*ages


# In[6]:


ages+100


# In[7]:


ages*2


# In[8]:


pd.Series([1,100])


# In[9]:


ages+pd.Series([1,100])


# In[10]:


rev_ages=ages.sort_index(ascending=False)
rev_ages


# In[11]:


ages*2


# In[12]:


ages+rev_ages

