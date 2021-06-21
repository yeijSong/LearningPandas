
# coding: utf-8

# In[7]:


import pandas as pd

file_path='C:/_WSHongIk2021/DataSet/read_csv_sample.csv'

df1=pd.read_csv(file_path)
print(df1,'\n')
print(type(df1))


# In[9]:


df2=pd.read_csv('./../DataSet/read_csv_sample.csv')


# In[10]:


print(df2)

