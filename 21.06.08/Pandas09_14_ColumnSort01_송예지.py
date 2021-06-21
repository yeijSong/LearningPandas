
# coding: utf-8

# In[1]:


import pandas as pd

deptDB=pd.read_csv('./../data/sawonDB/deptDB.csv',
                   names=['deptno','dname','loc'],header=None)
sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',
                    names=['sabun','saname','deptno','sajob',
                           'sapay','sahire','sasex','samgr'],header=None)
gogekDB=pd.read_csv('./../data/sawonDB/gogekDB.csv',
                    names=['gobun','goname','gotel','gojumin','godam'],header=None)


# In[2]:


deptDB['dname']=deptDB['dname'].str.strip("' ")
deptDB['loc']=deptDB['loc'].str.strip("' ")

sawonDB['saname']=sawonDB['saname'].str.strip("' ")
sawonDB['sajob']=sawonDB['sajob'].str.strip("' ")
sawonDB['sahire']=sawonDB['sahire'].str.strip("' ")
sawonDB['sasex']=sawonDB['sasex'].str.strip("' ")

gogekDB['goname']=gogekDB['goname'].str.strip("' ")
gogekDB['gotel']=gogekDB['gotel'].str.strip("' ")
gogekDB['gojumin']=gogekDB['gojumin'].str.strip("' ")


# In[3]:


deptDB


# In[4]:


sawonDB


# In[5]:


gogekDB


# In[6]:


deptSawon=deptDB.merge(sawonDB, how='inner', on='deptno')
deptSawon.head(2)


# In[7]:


columnSort=sawonDB.columns.sort_values(ascending=True)
columnSort


# In[8]:


sawonDB[columnSort]

