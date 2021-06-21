
# coding: utf-8

# ### Q.연도별로 그룹화하여 기대수명에 대한 평균을 구하고 그래프를 그리시오.

# In[2]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[3]:


print(df.head(n=3))


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[5]:


global_yearly_life_expectancy=df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)


# In[6]:


global_yearly_life_expectancy.plot()

