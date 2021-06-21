
# coding: utf-8

# ### 1.25_df to number

# In[1]:


import pandas as pd

scientists=pd.read_csv('./../data/scientists.csv')
scientists


# In[3]:


ages=scientists['Age']
ages.max()


# In[4]:


ages.mean()


# In[5]:


ages[ages>ages.mean()]


# In[6]:


ages>ages.mean()


# In[7]:


type(ages>ages.mean())


# In[8]:


manual_bool_values=[True,True,False,False,True,True,False,True]
ages[manual_bool_values]

