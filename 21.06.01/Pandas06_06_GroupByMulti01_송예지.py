
# coding: utf-8

# ### Q.연도별로 그룹화하고 그 그룹을 다시 대륙별로 그룹화하여 기대수명에 대한 평균을 구하시오(2가지 방법으로)

# In[1]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[2]:


print(df.head(n=3))


# In[7]:


multi_group_var= df.groupby(['year','continent'])['lifeExp']
print(multi_group_var)
print('-'*50)
print(multi_group_var.mean())
print('-'*50)
print(multi_group_var.mean().count())

