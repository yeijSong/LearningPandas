
# coding: utf-8

# ## 시리즈와 데이터프레임의 데이터 처리하기(p67)
# to_형태는 convert하겠다는 의미

# In[1]:


import pandas as pd

scientists=pd.read_csv('./../data/scientists.csv')
scientists


# In[2]:


print(scientists['Born'].dtype)
print(scientists['Died'].dtype)


# In[6]:


born_datetime=pd.to_datetime(scientists['Born'],format='%Y-%m-%d')
born_datetime


# In[7]:


died_datetime=pd.to_datetime(scientists['Died'],format='%Y-%m-%d')
died_datetime


# In[8]:


died_datetime2=died_datetime-born_datetime
died_datetime2


# In[10]:


scientists['born_dt'],scientists['died_dt']=(born_datetime,died_datetime)
scientists.head()


# In[12]:


scientists.shape


# In[13]:


scientists['age_days_dt']=(scientists['died_dt']-scientists['born_dt'])
scientists

