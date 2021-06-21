
# coding: utf-8

# ### 1.10_ select_column01

# In[1]:


import pandas as pd

exam_data={'이름':['서준','우현','인아'],
          '수학':[90,80,70],
          '영어':[98,89,95],
          '음악':[85,95,100],
          '체육':[100,90,90]}

df=pd.DataFrame(exam_data)
print(df)
print()
print(type(df))


# In[2]:


math1=df['수학']
print(math1)
print()
print(type(math1))
print('-'*20)

english=df.영어
print(english)
print()
print(type(english))
print('-'*20)


# ### 1.10_ select_column02

# In[3]:


music_gym=df[['음악','체육']]
print(music_gym)
print()
print(type(music_gym))
print('-'*20)

math2=df['수학']
print(math2)
print()
print(type(math2))
print('-'*20)

