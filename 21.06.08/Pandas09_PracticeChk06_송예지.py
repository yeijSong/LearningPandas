
# coding: utf-8

# ## Series.str.contains

# In[1]:


import pandas as pd

s1=pd.Series(['Mouse','dog','house and parrot','23'])
s1.str.contains('og')


# In[2]:


ind=pd.Index(['Mouse','dog','23house and parrot','23.0'])
ind.str.contains('23')


# In[4]:


s1.str.contains('oG')


# In[5]:


s1.str.contains('oG',case=False)


# In[6]:


s1.str.contains('house|dog')


# In[7]:


s1.str.contains('\\d')


# In[9]:


s2=pd.Series(['40','40.0','41','41.0','35'])
s2.str.contains('.0')


# In[10]:


s2.str.contains('0')

