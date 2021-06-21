
# coding: utf-8

# ## Q. 최대, 최소 기대수명 출력하라. [loc,iloc,컬럼명 3가지 이용]

# In[1]:


import pandas as pd

df=pd.read_csv('./../data/gapminder.tsv',sep='\t')
df


# In[2]:


df.head(2)


# In[3]:


subset_loc=df.loc[0]
subset_tail=df.tail(1)
subset_head=df.head(1)


# In[4]:


print(subset_loc,'\n===>')
print(subset_tail,'\n')

print(type(subset_loc))
print(type(subset_tail))
print(type(subset_head))

