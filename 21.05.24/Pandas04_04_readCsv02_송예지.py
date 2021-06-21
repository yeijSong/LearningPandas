
# coding: utf-8

# In[1]:


import pandas as pd

file_path='C:/_WSHongIk2021/DataSet/read_csv_sample.csv'

df1=pd.read_csv(file_path)
print(df1,'\n')
print(type(df1))


# In[2]:


df2=pd.read_csv('./../DataSet/read_csv_sample.csv')


# In[3]:


print(df2)


# In[4]:


df3=pd.read_csv(file_path, header=None)
print(df3,'\n')


# In[5]:


df4=pd.read_csv(file_path, index_col=None)
print(df4,'\n')


# In[6]:


df5=pd.read_csv(file_path, index_col='c0')
print(df5)


# In[7]:


df6=pd.read_csv(file_path, index_col=header)

