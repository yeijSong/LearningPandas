
# coding: utf-8

# ## 데이터프레임의 열 삭제하기

# In[1]:


import pandas as pd

scientists=pd.read_csv('./../data/scientists.csv')
scientists


# In[2]:


scientists.columns


# In[3]:


scientists_dropped=scientists.drop(['Age'],axis=1)
scientists_dropped.columns

