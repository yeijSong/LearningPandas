
# coding: utf-8

# In[6]:


import pandas as pd

url='./../DataSet/Test01.html'

tables=pd.read_html(url)


# In[9]:


print(len(tables))


# In[14]:


print(tables)


# In[18]:


for i in range(len(tables)):
    print('tables[%s]'%i,'\n')
    print(tables[i])
    print('-'*30)


# In[19]:


df=tables[1]
print(df.columns)

