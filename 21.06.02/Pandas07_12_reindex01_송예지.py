
# coding: utf-8

# ### 1.17_ reindex

# 결측치는 어떤 계산을 해도 결과값이 결측치로 나온다.
# 
# fill_value -> 결측치를 무엇으로 채워줄래

# In[1]:


import pandas as pd

dict_data={'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

df=pd.DataFrame(dict_data, index=['r0','r1','r2'])
df


# 기존 데이터에 존재하지 않았던 행을 reindex하면 결측치로 나온다

# In[2]:


new_index=['r0','r1','r2','r3','r4']
ndf=df.reindex(new_index)
ndf


# In[3]:


new_index=['r0','r1','r2','r3','r4']
ndf2=df.reindex(new_index,fill_value=0)
ndf2

