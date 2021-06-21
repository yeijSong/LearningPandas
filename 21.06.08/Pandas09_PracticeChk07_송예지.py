
# coding: utf-8

# ## enumerate() 함수

# In[1]:


import pandas as pd

Animal=['오렌지','장미','바다','여우']


# In[4]:


for idx in Animal:
    print(idx)


# In[5]:


for a,b in enumerate(Animal):
    print(a,b)


# In[6]:


for a,b in enumerate(Animal,0):
    print(a,b)


# In[7]:


for a,b in enumerate(Animal,11):
    print(a,b)

