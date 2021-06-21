
# coding: utf-8

# In[4]:


import pandas as pd

df=pd.DataFrame({'float':[1.0],
                 'int':[1],
                 'datetime':[pd.Timestamp('20180310')],
                 'string':['foo']})


# In[5]:


print(df)


# In[8]:


print(type(df))


# In[7]:


df.dtypes

