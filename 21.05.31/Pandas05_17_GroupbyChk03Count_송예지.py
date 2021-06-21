
# coding: utf-8

# ### 1.lifeExp열을 연도별로 그룹화하여 평균 계산하기

# In[29]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[30]:


print(df.head(n=10))


# In[31]:


df.groupby('year')['lifeExp'].mean()


# In[32]:


df['year'].unique()


# In[33]:


uniList=df['year'].unique()
print(type(uniList))
print()
print(uniList)


# ### 2. 기대수명 연도별 개수 확인하기

# In[34]:


for idx in uniList:
    print(idx,'=====>①')
    grYear=df[df['year']==idx]
    print(len(grYear),'=====>② \n:',grYear.head(3),'=====>③ \n:',grYear.shape)
    print(grYear['lifeExp'].mean())


# In[35]:


print(len(uniList)*grYear.shape[0])


# ### 3. 대륙별 연도 개수 확인하기

# In[36]:


df.groupby('continent')['year'].count()


# In[37]:


df['continent'].unique()


# In[38]:


uniList2=df['continent'].unique()
uniList2


# In[39]:


for idx in uniList2:
    print(idx,'=====>①')
    grContinent=df[df['continent']==idx]
    print(len(grContinent),'=====>② \n:',grContinent.head(3),'=====>③ \n:',grContinent.shape)
    print(grContinent['year'].count())


# In[45]:




