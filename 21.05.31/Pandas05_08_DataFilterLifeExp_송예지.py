
# coding: utf-8

# ## Q. 최대, 최소 기대수명 출력하라. [loc,iloc,컬럼명 3가지 이용]

# In[22]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')
df


# ### 1. column명 이용하기

# In[23]:


lifeExp_df=df['lifeExp']
print(lifeExp_df)


# In[24]:


print('최대 기대수명은 %0.3f입니다.'%lifeExp_df.max())
print('최소 기대수명은 %0.3f입니다.'%lifeExp_df.min())


# ### 2. loc 이용하기

# In[28]:


lifeExp_df2=df.loc[:,['lifeExp']]
print(lifeExp_df2)


# In[29]:


print('최대 기대수명은 %0.3f입니다.'%lifeExp_df2.max())
print('최소 기대수명은 %0.3f입니다.'%lifeExp_df2.min())


# ### 3. iloc 이용하기

# In[30]:


lifeExp_df3=df.iloc[:,3]
print(lifeExp_df3)


# In[31]:


print('최대 기대수명은 %0.3f입니다.'%lifeExp_df3.max())
print('최소 기대수명은 %0.3f입니다.'%lifeExp_df3.min())

