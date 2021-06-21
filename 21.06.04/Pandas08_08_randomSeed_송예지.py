
# coding: utf-8

# ## 시리즈와 데이터프레임의 데이터 섞기

# In[1]:


import pandas as pd

scientists=pd.read_csv('./../data/scientists.csv')
scientists


# In[2]:


scientists['Age']


# In[24]:


import random

random.seed(10)
print(random.random())


# In[26]:


random.seed(20)
print(random.random())


# In[27]:


random.seed(30)
print(random.random())

