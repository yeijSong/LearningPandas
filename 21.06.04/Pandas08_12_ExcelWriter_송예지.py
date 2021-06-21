
# coding: utf-8

# ## 2.9 to excel

# In[1]:


import pandas as pd

data={'name':['Jerry','Riah','Paul'],
     'algol':['A','A+','B'],
     'basic':['C','B','B+'],
     'c++':['B+','C','C+']}

df=pd.DataFrame(data)
df.set_index('name',inplace=True)
print(df)

df.to_excel('./../data/df_sample.xlsx')


# ## 2.10 ExcelWriter

# In[2]:


data01={'name':['Jerry','Riah','Paul'],
     'algol':['A','A+','B'],
     'basic':['C','B','B+'],
     'c++':['B+','C','C+']}

data02={'c0':[1,2,3],
       'c1':[4,5,6],
       'c2':[7,8,9],
       'c3':[10,11,12],
       'c4':[13,14,15]}

df1=pd.DataFrame(data01)
df1.set_index('name',inplace=True)
df1


# In[4]:


df2=pd.DataFrame(data02)
df2.set_index('c0',inplace=True)
df2


# In[5]:


writer=pd.ExcelWriter('./../data/df_excelwriter.xlsx')
df1.to_excel(writer,sheet_name='시트1')
df2.to_excel(writer,sheet_name='시트2')
writer.save()

