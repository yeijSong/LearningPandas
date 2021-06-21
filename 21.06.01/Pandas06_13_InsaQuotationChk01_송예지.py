
# coding: utf-8

# In[15]:


import pandas as pd

deptDB=pd.read_csv('./../data/sawonDB/deptDB.csv',names=['deptno','dname','loc'],header=None)
sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',names=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'],header=None)
gogekDB=pd.read_csv('./../data/sawonDB/gogekDB.csv',names=['gobun','goname','gotel','gojumin','godam'],header=None)


# In[16]:


deptDB


# In[17]:


sawonDB


# In[18]:


gogekDB


# In[35]:


deptDB=deptDB.replace("\'",'', regex = True)
deptDB


# In[36]:


sawonDB=sawonDB.replace("\'",'', regex = True)
sawonDB


# In[37]:


gogekDB=gogekDB.replace("\'",'', regex = True)
gogekDB

