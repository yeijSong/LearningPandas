
# coding: utf-8

# ### 1 - 05

# In[1]:


import pandas as pd

df=pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
               index=['준서','예은'],
               columns=['나이','성별','학교'])

print(df,'\n')
print(df.index,'\n')
print(df.columns,'\n')


# In[2]:


df.index=['학생1','학생2']
df.columns=['연령','남녀','소속']

print(df,'\n')
print(df.index,'\n')
print(df.columns,'\n')


# #### 원본 객체를 변경하려면 inplace=True옵션을 사용한다.

# In[3]:


df=pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
               index=['준서','예은'],
               columns=['나이','성별','학교'])

print(df)
print('-'*30)
redf=df.rename(columns={'나이':'연령','성별':'남녀','학교':'소속'})
df.rename(index={'준서':'학생1','예은':'학생2'})
print(redf)
print('-'*30)
print(df)
print('-'*30)
df.rename(columns={'나이':'연령','성별':'남녀','학교':'소속'},inplace=True)
df.rename(index={'준서':'학생1','예은':'학생2'},inplace=True)
print(df)

