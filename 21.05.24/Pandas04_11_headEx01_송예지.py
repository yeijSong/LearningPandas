
# coding: utf-8

# ### 데이터 불러오기###
# 
# - df라는 변수에 저장
# - 데이터 추출/불러온 데이터 확인하기/
# - head : 데이터 프레임에서 가장 앞에 있는 5개의 행을 출력한다.
# 
# - head, tail, info, type, dtypes, shape, index, columns

# In[2]:


import pandas as pd

df=pd.DataFrame({'animal':['alligator','bee','falcon',
                           'lion','monkey','parrot','shark','whale','zebra']})


# In[3]:


print(df)


# In[4]:


print(df.head())


# In[5]:


print(df.head(3))


# In[6]:


print(df.head(-4))

