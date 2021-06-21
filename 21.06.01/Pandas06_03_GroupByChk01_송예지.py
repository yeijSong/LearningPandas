
# coding: utf-8

# In[3]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')
df


# In[4]:


type(df)


# In[7]:


type(df['pop'])


# In[8]:


grouped_year_df=df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df['pop'])


# In[6]:


grouped_year_df['pop'].mean()

