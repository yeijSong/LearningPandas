
# coding: utf-8

# ## 시리즈와 데이터프레임의 데이터 섞기

# In[1]:


import pandas as pd

scientists=pd.read_csv('./../data/scientists.csv')
scientists


# In[2]:


scientists['Age']


# In[2]:


import random

random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])


# In[3]:


random.shuffle(scientists['Age'])
random.seed(42)
print(scientists['Age'])

