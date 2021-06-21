
# coding: utf-8

# ### 1.25_df_to_number
# 
# 여기에서는 Seaborn라이브러리에서 제공하는 데이터셋2 중에서
# 타이타닉(titanic)데이터 셋을 사용한다.

# In[4]:


import pandas as pd
import seaborn as sns

titanic=sns.load_dataset('titanic')
titanic


# ## Q1. 행렬 Chk

# In[3]:


titanic.shape


# ## Q2. 컬럼명 Chk

# In[5]:


titanic.columns


# ## Q3. 컬럼별 unique() Chk

# In[30]:


print('===== 컬럼별 unique() 체크하기 =====')
for i in titanic.columns:
    print(titanic[i].unique())


# ## Q4. 나이의 최소, 최대

# In[14]:


print('타이타닉호 최고령자는 %d세입니다'%titanic['age'].max())
print('타이타닉호 최연소인은 %d세입니다'%titanic['age'].min())


# ## Q5. 성별에 따른 survived 개수

# In[23]:


titanic.groupby(['sex','survived'])['survived'].count()


# ## Q6. 남자, 여자 명수

# In[27]:


titanic.groupby('sex')['sex'].count()

