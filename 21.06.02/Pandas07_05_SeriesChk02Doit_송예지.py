
# coding: utf-8

# ## 시리즈와 데이터 프레임 직접 만들기(p51)
# ### 1. 시리즈 만들기

# In[1]:


import pandas as pd
s=pd.Series(['banana',42])
print(s)


# In[2]:


s=pd.Series(['Wes McKinney','creator of pandas'])
print(s)


# In[3]:


s=pd.Series(['Wes McKinney','creator of pandas'],index=['person','who'])
print(s)


# ### 2. 데이터 프레임 만들기

# In[5]:


scientists=pd.DataFrame({'name':['Rosaline Franklin','William Gosset'],
                        'Occupation':['Chemist','Statistician'],
                        'Born':['1920-07-25','1876-06-13'],
                        'Died':['1958-04-16','1937-10-16'],
                        'Age':[37,61]})
scientists


# In[6]:


scientists=pd.DataFrame({'Occupation':['Chemist','Statistician'],
                        'Born':['1920-07-25','1876-06-13'],
                        'Died':['1958-04-16','1937-10-16'],
                        'Age':[37,61]},
                       index=['Rosaline Franklin','William Gosset'],
                       columns=['Occupation','Born','Died','Age'])
scientists


# In[8]:


from collections import OrderedDict

scientists=pd.DataFrame([('name',['Rosaline Franklin','William Gosset']),
                        ('Occupation',['Chemist','Statistician']),
                        ('Born',['1920-07-25','1876-06-13']),
                        ('Died',['1958-04-16','1937-10-16']),
                        ('Age',[37,61])])
scientists


# In[9]:


type(scientists[0])


# In[10]:


from collections import OrderedDict

scientists=pd.DataFrame(OrderedDict([
    ('name',['Rosaline Franklin','William Gosset']),
    ('Occupation',['Chemist','Statistician']),
    ('Born',['1920-07-25','1876-06-13']),
    ('Died',['1958-04-16','1937-10-16']),
    ('Age',[37,61])
]))
scientists

