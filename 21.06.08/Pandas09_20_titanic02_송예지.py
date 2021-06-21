
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns

titanic=sns.load_dataset('titanic')
titanic


# In[3]:


titanic.info()


# In[4]:


titanic.dtypes


# ## Q4. 나이의 최소, 최대

# In[16]:


print('타이타닉호 최고령자는 %.2f세입니다'%titanic['age'].max())
print('타이타닉호 최연소인은 %.2f세입니다'%titanic['age'].min())


# ## Q5. 성별에 따른 survived 개수

# In[9]:


titanic.groupby(['sex','survived'])['survived'].count()


# In[17]:


survived_bySex=titanic[titanic['survived']==1]
survived_bySex.groupby('sex')['sex'].count()

