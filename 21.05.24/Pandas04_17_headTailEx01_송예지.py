
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.DataFrame({'Animal':['Falcon','Falcon','Parrot','Parrot'],
                 'Max Speed':[380.,370.,24.,26.]})
df


# In[3]:


df.groupby(['Animal']).mean()


# In[8]:


df1=pd.read_csv('./../data/gapminder.tsv',sep='\t')
print(df1)


# In[9]:


print(df.shape)
print(df.shape[0])
print(df.shape[1])


# In[10]:


len(df)


# In[11]:


df.head()


# In[12]:


df[0:5]


# In[13]:


df.head(n=7)


# In[14]:


df.tail()


# In[15]:


df[len(df)-5:len(df)+1]


# In[17]:


df.tail(n=7)

