
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

# In[5]:


print('===== 컬럼별 unique() 체크하기 =====')
for i in titanic.columns:
    print('< %s 그룹 >'%i)
    print(titanic[i].unique())

