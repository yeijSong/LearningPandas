
# coding: utf-8

# ### 1.25_df to number

# In[1]:


import pandas as pd
import seaborn as sns

titanic=sns.load_dataset('titanic')
print(titanic.columns,'\n\n',titanic.shape)


# In[2]:


df=titanic.loc[:,['age','fare']]
print(df.head(),'\n\n')
print(type(df))


# In[3]:


addition=df+10
print(addition.head(),'\n\n')
print(type(addition))


# ### 1.26 df to df

# In[4]:


print(df.tail(),'\n\n')
print(type(df),'\n\n',df.shape)


# In[5]:


addition=df+10
print(addition.tail(),'\n\n')
print(type(addition))


# In[6]:


substraction=addition-df
print(substraction.tail(),'\n\n')
print(type(substraction))

