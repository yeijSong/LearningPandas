
# coding: utf-8

# ### Q.연도별로 그룹화하고 그 그룹을 다시 대륙별로 그룹화하여 기대수명에 대한 평균을 구하시오(2가지 방법으로)

# In[3]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[4]:


print(df.head(n=3))


# #### < 방법 1 : built-in 함수 >

# In[5]:


multi_group_var= df.groupby(['year','continent'])['lifeExp','pop']
print(multi_group_var)
print('-'*50)
print(multi_group_var.mean())
print('-'*50)
print(multi_group_var.mean().count())


# #### < 방법 2 >

# In[6]:


yearList=df['year'].unique()
contiList=df['continent'].unique()
print(yearList)
print(contiList)


# In[7]:


for i in yearList:
    grYear=df[df['year']==i]
    print('-'*60)
    for j in contiList:
        grConti=grYear[grYear['continent']==j]
        print(grConti[['lifeExp','pop']].mean())


# ### 그룹화한 데이터의 개수 세기

# In[8]:


print(df.groupby('continent')['country'])


# In[9]:


print(df.groupby('continent')['country'].nunique())
print('-'*50)
print(df.groupby('continent')['country'].unique())
print('-'*50)
print(df.groupby('continent')['country'].unique()['Oceania'])
print('-'*50)
print(df.groupby('continent')['country'].count())
print('-'*50)
print(df.groupby('continent')['country'].count()['Africa'])

