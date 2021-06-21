
# coding: utf-8

# ## pandas.merge
# database-style join
# 
# * how='left'(왼쪽 레코드는 모두 가져오고 오른쪽에는 일치하는 것만)
# * how='right'(오른쪽 레코드는 모두 가져오고 왼쪽에는 일치하는 것만)
# * how='inner'(매치되는 것 끼리 가져와 달라)
# 
# * on=연결할 기준이 되는 column

# In[1]:


import pandas as pd

df1=pd.DataFrame({'lkey':['foo','bar','baz','foo'],
                 'value':[1,2,3,5]})
df2=pd.DataFrame({'rkey':['foo','bar','baz','foo'],
                 'value':[5,6,7,8]})


# In[3]:


print(df1)
print()
print(df2)


# In[9]:


df1=pd.DataFrame({'a':['foo','bar'],'b':[1,2]})
df2=pd.DataFrame({'a':['foo','baz'],'c':[3,4]})


# In[10]:


print(df1)
print()
print(df2)


# In[11]:


df1.merge(df2, how='inner',on='a')


# In[12]:


df1.merge(df2, how='left',on='a')


# In[13]:


df1.merge(df2, how='right',on='a')

