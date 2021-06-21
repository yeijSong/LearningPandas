
# coding: utf-8

# In[1]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[3]:


number_of_rows=df.shape[0]
print(number_of_rows,'\n\n')

last_row_index=number_of_rows-1
print(df.loc[last_row_index])


# In[4]:


print(df.loc[len(df)-1])


# In[5]:


df.tail(n=1)


# In[6]:


df.tail(n=2)


# In[7]:


df.loc[[0,99,999]]

