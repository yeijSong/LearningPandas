
# coding: utf-8

# ## 불린 추출과 브로드캐스팅(p65)

# In[4]:


import pandas as pd

scientists=pd.read_csv('./../data/scientists.csv')
scientists


# In[7]:


scientists[scientists['Age']>scientists['Age'].mean()]


# In[8]:


scientists.loc[[True,True,False,True]]


# In[10]:


scientists*2

