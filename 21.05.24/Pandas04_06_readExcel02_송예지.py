
# coding: utf-8

# In[2]:


import pandas as pd

df1=pd.read_excel('./../DataSet/datalabPractice01.xlsx')
df2=pd.read_excel('./../DataSet/datalabPractice01.xlsx',                    sheet_name='Sheet1', usecols=[0,1,2],skiprows=[0],                    skipfooter=2, header=None)


# In[3]:


print(df2.columns)


# In[4]:


print(df2)


# In[5]:


print(df1)


# In[7]:


df3=pd.read_excel('./../DataSet/datalabPractice01.xlsx',                    sheet_name='Sheet1', usecols=[0,1,2],skiprows=[0],                    skipfooter=3, header=None)


# In[8]:


print(df3)

