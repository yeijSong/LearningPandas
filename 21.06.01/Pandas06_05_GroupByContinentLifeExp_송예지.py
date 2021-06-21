
# coding: utf-8

# ### Q.대륙별로 그룹화하여 기대수명에 대한 평균을 구하시오(2가지 방법으로)

# In[2]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[3]:


print(df.head(n=3))


# #### < 방법 1 >

# In[4]:


df.groupby('continent')['lifeExp'].mean()


# #### < 방법 2 >

# In[8]:


df['continent'].unique()


# In[9]:


contiList=df['continent'].unique()
print(contiList)


# In[13]:


for idx in contiList:
    print(idx,'=====>①continent')
    grConti=df[df['continent']==idx]
    print(len(grConti),'=====>②continentNum \n:',grConti.head(3),'=====>③ \n:',grConti.shape)
    print(grConti['lifeExp'].mean())
    print('-'*100)

