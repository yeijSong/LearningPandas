
# coding: utf-8

# In[84]:


import pandas as pd

deptDB=pd.read_csv('./../data/sawonDB/deptDB.csv',
                   names=['deptno','dname','loc'],header=None)
sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',
                    names=['sabun','saname','deptno','sajob',
                           'sapay','sahire','sasex','samgr'],header=None)
gogekDB=pd.read_csv('./../data/sawonDB/gogekDB.csv',
                    names=['gobun','goname','gotel','gojumin','godam'],header=None)


# In[85]:


deptDB


# In[86]:


deptDB['dname']=deptDB['dname'].str.strip("' ")
deptDB['loc']=deptDB['loc'].str.strip("' ")


# In[87]:


deptDB


# In[88]:


sawonDB['saname']=sawonDB['saname'].str.strip("' ")
sawonDB['sajob']=sawonDB['sajob'].str.strip("' ")
sawonDB['sahire']=sawonDB['sahire'].str.strip("' ")
sawonDB['sasex']=sawonDB['sasex'].str.strip("' ")


# In[89]:


sawonDB


# In[90]:


gogekDB


# In[91]:


gogekDB['goname']=gogekDB['goname'].str.strip("' ")
gogekDB['gotel']=gogekDB['gotel'].str.strip("' ")
gogekDB['gojumin']=gogekDB['gojumin'].str.strip("' ")


# In[92]:


gogekDB


# ### Q1. sawonDB에서 입사년도가 88년도인 사원 출력

# In[94]:


print('입사년도가 88년도인 사원',end='\n===>')

for i in range(sawonDB['sahire'].count()):
    if int(sawonDB['sahire'][i][0:4])==1988:
        print(sawonDB['saname'][i],end='  ')
    else:
        pass


# In[95]:


print('입사년도가 88년도인 사원 리스트')
print('-'*70)

for i in range(sawonDB['sahire'].count()):
    if int(sawonDB['sahire'][i][0:4])==1988:
        print(sawonDB.iloc[[i]])
    else:
        pass


# ### Q2. sawonDB에서 4월에 입사한 사원 출력

# In[96]:


print('4월에 입사한 사원',end='\n===>')

for i in range(sawonDB['sahire'].count()):
    if int(sawonDB['sahire'][i][6])==4:
        print(sawonDB['saname'][i],end='  ')
    else:
        pass


# In[97]:


print('4월에 입사한 사원 리스트')
print('-'*70)

for i in range(sawonDB['sahire'].count()):
    if int(sawonDB['sahire'][i][6])==4:
        print(sawonDB.iloc[[i]])
    else:
        pass

