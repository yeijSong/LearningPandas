
# coding: utf-8

# In[2]:


import pandas as pd

deptDB=pd.read_csv('./../data/sawonDB/deptDB.csv',
                   names=['deptno','dname','loc'],header=None)
sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',
                    names=['sabun','saname','deptno','sajob',
                           'sapay','sahire','sasex','samgr'],header=None)
gogekDB=pd.read_csv('./../data/sawonDB/gogekDB.csv',
                    names=['gobun','goname','gotel','gojumin','godam'],header=None)


# In[3]:


deptDB['dname']=deptDB['dname'].str.strip("' ")
deptDB['loc']=deptDB['loc'].str.strip("' ")

sawonDB['saname']=sawonDB['saname'].str.strip("' ")
sawonDB['sajob']=sawonDB['sajob'].str.strip("' ")
sawonDB['sahire']=sawonDB['sahire'].str.strip("' ")
sawonDB['sasex']=sawonDB['sasex'].str.strip("' ")

gogekDB['goname']=gogekDB['goname'].str.strip("' ")
gogekDB['gotel']=gogekDB['gotel'].str.strip("' ")
gogekDB['gojumin']=gogekDB['gojumin'].str.strip("' ")


# In[4]:


deptDB


# In[5]:


sawonDB


# In[6]:


gogekDB


# In[9]:


deptSawon=deptDB.merge(sawonDB, how='inner', on='deptno')
deptSawon.head(2)


# In[11]:


deptno30=deptSawon[deptSawon['dname']=='전산부']
print('전산부 직원의 평균 연봉 :',deptno30['sapay'].mean())

