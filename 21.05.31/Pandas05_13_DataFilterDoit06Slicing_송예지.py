
# coding: utf-8

# ### 데이터 추출하기-슬라이싱 구문,range메서드(p39)

# #### 4. 슬라이싱 구문으로 원하는 데이터 추출하기

# In[1]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')
df


# In[2]:


subset=df.iloc[:,:3]
print(subset.head())


# In[3]:


subset2=df.iloc[:,0:6:2]
print(subset2.head())


# #### 5.loc/iloc 속상 자유자재로 사용하기

# In[4]:


df.head(3)


# In[5]:


df.iloc[[0,99,999],[0,3,5]]


# In[8]:


df.loc[[0,99,999],['country','lifeExp','gdpPercap']]


# In[10]:


df.loc[10:13,['country','lifeExp','gdpPercap']]


# In[11]:


df.iloc[10:13,[0,3,-1]]

