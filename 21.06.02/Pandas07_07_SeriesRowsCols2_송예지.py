
# coding: utf-8

# ### 1.11_ select_element01

# In[1]:


import pandas as pd

exam_data={'이름':['서준','우현','인아'],
          '수학':[90,80,70],
          '영어':[98,89,95],
          '음악':[85,95,100],
          '체육':[100,90,90]}

df=pd.DataFrame(exam_data)
print(df)


# In[2]:


df.set_index('이름',inplace=True)
print(df)
print('-'*20)

a=df.loc['서준','음악']
print(a)
print('-'*20)
b=df.iloc[0,2]
print(b)


# ### 1.10_ select_element02

# In[3]:


c=df.loc['서준',['음악','체육']]
print(c)
print('-'*20)
d=df.iloc[0,[2,3]]
print(d)
print('-'*20)
e=df.loc['서준','음악':'체육']
print(e)
print('-'*20)
f=df.iloc[0,2:]
print(f)


# In[5]:


g=df.loc[['서준','우현'],['음악','체육']]
print(g)
print('-'*20)
h=df.iloc[[0,1],[2,3]]
print(h)
print('-'*20)
i=df.loc['서준':'우현','음악':'체육']
print(i)
print('-'*20)
j=df.iloc[0:2,2:]
print(j)


# In[6]:


df.loc[:,['음악','체육']]


# In[7]:


print(df)
df.iloc[:,[2,3]]


# In[9]:


df.iloc[:,2:4]

