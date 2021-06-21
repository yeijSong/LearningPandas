
# coding: utf-8

# ### 1.lifeExp열을 연도별로 그룹화하여 평균 계산하기

# In[3]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[2]:


print(df.head(n=10))


# In[4]:


df.groupby('year')['lifeExp'].mean()


# In[5]:


df['year'].unique()


# In[7]:


uniList=df['year'].unique()
print(type(uniList))
print()
print(uniList)

