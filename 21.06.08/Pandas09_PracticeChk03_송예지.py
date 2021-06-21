
# coding: utf-8

# In[13]:


import pandas as pd

deptDB=pd.read_csv('./../data/sawonDB/deptDB.csv',
                   names=['deptno','dname','loc'],header=None)
sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',
                    names=['sabun','saname','deptno','sajob',
                           'sapay','sahire','sasex','samgr'],header=None)
gogekDB=pd.read_csv('./../data/sawonDB/gogekDB.csv',
                    names=['gobun','goname','gotel','gojumin','godam'],header=None)


# In[14]:


deptDB


# In[15]:


sawonDB


# In[16]:


gogekDB


# ### Q1. sawonDB에서 입사년도가 88년도인 사원 출력

# In[17]:


print('입사년도가 88년도인 사원',end='\n===>')

for i in range(sawonDB2['sahire'].count()):
    if sawonDB2['sahire'].str.strip()[i][0:4]=='1988':
        print(sawonDB2['saname'][i],end='  ')
    else:
        pass


# In[18]:


print('입사년도가 88년도인 사원 리스트')
print('-'*70)

for i in range(sawonDB2['sahire'].count()):
    if int(sawonDB2['sahire'].str.strip()[i][0:4])==1988:
        print(sawonDB2.iloc[[i]])
    else:
        pass

