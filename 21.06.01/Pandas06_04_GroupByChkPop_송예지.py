
# coding: utf-8

# In[9]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')


# In[10]:


print(df.head(n=3))


# In[11]:


df.groupby('year')['pop'].mean()


# In[12]:


df['year'].unique()


# In[13]:


yearList=df['year'].unique()
print(type(yearList))
print()
print(yearList)


# In[14]:


for idx in yearList:
    print(idx,'=====>①')
    grYear=df[df['year']==idx]
    print(len(grYear),'=====>② \n:',grYear.head(3),'=====>③ \n:',grYear.shape)
    print(grYear['pop'].mean())

