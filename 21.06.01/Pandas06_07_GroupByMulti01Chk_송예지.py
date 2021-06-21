
# coding: utf-8

# ### Q.연도별로 그룹화하고 그 그룹을 다시 대륙별로 그룹화하여 기대수명에 대한 평균을 구하시오(2가지 방법으로)

# In[3]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[4]:


print(df.head(n=3))


# #### < 방법 1 >

# In[5]:


multi_group_var= df.groupby(['year','continent'])['lifeExp']
print(multi_group_var)
print('-'*50)
print(multi_group_var.mean())
print('-'*50)
print(multi_group_var.mean().count())


# #### < 방법 2 >

# In[7]:


yearList=df['year'].unique()
contiList=df['continent'].unique()
print(yearList)
print(contiList)


# In[31]:


for i in yearList:
    grYear=df[df['year']==i]
    print('-'*60)
    for j in contiList:
        grConti=grYear[grYear['continent']==j]
        print('%d년 %10s 기대수명 평균 : ' %(i,j),end=' ')
        print(grConti['lifeExp'].mean())

