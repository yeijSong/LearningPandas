
# coding: utf-8

# ### 데이터 프레임에서 시리즈 선택하기(p54)

# In[1]:


import pandas as pd

scientists=pd.DataFrame(
    data={'Occupation':['Chemist','Statistician'],
            'Born':['1920-07-25','1876-06-13'],
            'Died':['1958-04-16','1937-10-16'],
            'Age':[37,61]},
    index=['Rosaline Franklin','William Gosset'],
    columns=['Occupation','Born','Died','Age'])
scientists


# In[2]:


first_row=scientists.loc['William Gosset']
type(first_row)


# In[3]:


first_row


# In[14]:


first_row.index


# In[5]:


first_row.values


# In[6]:


first_row.keys()


# In[7]:


first_row.index[0]


# In[8]:


first_row.keys()[0]


# ### 시리즈의 mean, min,std메서드 사용하기(p56)

# In[9]:


ages=scientists['Age']
ages


# In[10]:


ages.mean()


# In[11]:


ages.min()


# In[12]:


ages.max()


# In[13]:


ages.std()

