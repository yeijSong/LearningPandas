
# coding: utf-8

# In[18]:


import pandas as pd

deptDB=pd.read_csv('./../data/sawonDB/deptDB.csv',names=['deptno','dname','loc'],header=None)
sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',names=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'],header=None)
gogekDB=pd.read_csv('./../data/sawonDB/gogekDB.csv',names=['gobun','goname','gotel','gojumin','godam'],header=None)


# In[19]:


deptDB


# In[11]:


sawonDB


# In[12]:


gogekDB

