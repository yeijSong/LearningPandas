
# coding: utf-8

# axis
# 
# 0이면 인덱스, 1이면 컬럼
# 디폴트값은 0
# 대부분 0이면 행이지만 아주 가끔 일관성 없이 0이 열인 경우도 있음

# In[2]:


import pandas as pd

exam_data={'수학':[90,80,70],'영어':[98,89,95],
          '음악':[85,95,100],'체육':[100,90,90]}

df=pd.DataFrame(exam_data)
print(df)
print('-'*30)
df=pd.DataFrame(exam_data,index=['서준','우현','인아'])
print(df)
print('-'*30)

df2=df[:]
df2.drop('우현',inplace=True)
print(df2)
print('-'*30)

df3=df[:]
df3.drop(['우현','인아'],axis=0,inplace=True)
print(df3)
print('-'*30)


# In[4]:


df4=df[:]
df4.drop('수학',axis=1,inplace=True)
print(df4)
print('-'*30)

df5=df[:]
df5.drop(['영어','음악'],axis=1,inplace=True)
print(df5)
print('-'*30)

