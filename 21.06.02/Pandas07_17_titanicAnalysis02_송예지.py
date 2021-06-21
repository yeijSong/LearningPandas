
# coding: utf-8

# ### 1.25_df_to_number
# 
# 여기에서는 Seaborn라이브러리에서 제공하는 데이터셋2 중에서
# 타이타닉(titanic)데이터 셋을 사용한다.

# In[2]:


import pandas as pd
import seaborn as sns

titanic=sns.load_dataset('titanic')
titanic


# In[3]:


titanic.info()


# In[4]:


titanic.dtypes


# ## Q1. 행렬 Chk

# In[5]:


titanic.shape


# ## Q2. 컬럼명 Chk

# In[6]:


titanic.columns


# ## Q3. 컬럼별 unique() Chk

# In[7]:


print('===== 컬럼별 unique() 체크하기 =====')
for i in titanic.columns:
    print(titanic[i].unique())


# ## Q4. 나이의 최소, 최대

# In[8]:


print('타이타닉호 최고령자는 %d세입니다'%titanic['age'].max())
print('타이타닉호 최연소인은 %d세입니다'%titanic['age'].min())


# ## Q5. 성별에 따른 survived 개수

# In[9]:


titanic.groupby(['sex','survived'])['survived'].count()


# ## Q6. 남자, 여자 명수

# In[10]:


titanic.groupby('sex')['sex'].count()


# ## Q7. 연령대별 사망자수 0~10/11~20/.../70~80 ->남/녀 사망자수

# In[11]:


type(titanic['age'][0])


# In[12]:


grAge=[]
grAgeIndex=['0~9','10~19','20~29','30~39','40~49','50~59','60~69','70~79','80~89']
for i in range(len(grAgeIndex)):
    grAge.append(titanic[titanic['age']//10==i])
    print(grAgeIndex[i],'\n',grAge[i].groupby('sex')['survived'].count())

