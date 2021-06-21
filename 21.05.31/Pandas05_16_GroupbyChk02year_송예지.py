
# coding: utf-8

# ### 1.lifeExp열을 연도별로 그룹화하여 평균 계산하기

# In[2]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[3]:


print(df.head(n=10))


# In[4]:


df.groupby('year')['lifeExp'].mean()


# In[5]:


df['year'].unique()


# In[6]:


uniList=df['year'].unique()
print(type(uniList))
print()
print(uniList)


# ### 2. 연도별 개수 확인하기

# In[7]:


for idx in uniList:
    print(idx,'=====>①')
    grYear=df[df['year']==idx]
    print(len(grYear),'=====>② \n:',grYear.head(3),'=====>③ \n:',grYear.shape)
    print(grYear['lifeExp'].mean())


# In[8]:


print(len(uniList)*grYear.shape[0])

