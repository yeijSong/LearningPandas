
# coding: utf-8

# ## 데이터프레임의 열 삭제하기

# In[2]:


import pandas as pd

data={'name':['Jerry','Riah','Paul'],
     'algol':['A','A+','B'],
     'basic':['C','B','B+'],
     'c++':['B+','C','C+']}

df=pd.DataFrame(data)
df.set_index('name',inplace=True)
print(df)

df.to_csv('./../data/df_sample.csv')

