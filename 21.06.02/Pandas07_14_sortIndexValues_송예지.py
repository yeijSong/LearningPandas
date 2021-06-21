
# coding: utf-8

# ### 1.19_ sort_index

# In[2]:


import pandas as pd

dict_data={'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

df=pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df)
print('-'*30)

ndf=df.sort_index(ascending=False)
ndf


# ### 1.20_ sort_values

# set_index와는 다르게 덮어쓰기가 아니고 계속 새로 생겨난다

# In[1]:


import pandas as pd

dict_data={'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

df=pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df)
print('-'*30)

ndf=df.sort_values(by='c1',ascending=False)
ndf

