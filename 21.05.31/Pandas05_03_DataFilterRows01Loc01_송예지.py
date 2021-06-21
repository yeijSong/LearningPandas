
# coding: utf-8

# In[1]:


import pandas as pd

df=pd.DataFrame([[1,2],[4,5],[7,8]], 
                index=['cobra','viper','sidewinder'], 
                columns=['max_speed','shield'])
df


# In[2]:


df.loc['viper']  # df.iloc[0]


# In[6]:


df.loc[0]


# In[5]:


df.loc[['viper', 'sidewinder']]


# In[7]:


df.loc['cobra', 'shield']


# In[8]:


df.loc['cobra':'viper', 'max_speed'] #loc에서는 인덱싱할 때 뒷부분이 포함된다


# In[8]:


df.loc[[False, False, True]]


# In[9]:


df.loc[df['shield']>6]


# In[10]:


df.loc[df['shield']>6,['max_speed']]

