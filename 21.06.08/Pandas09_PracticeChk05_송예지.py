
# coding: utf-8

# In[6]:


import pandas as pd

deptDB=pd.read_csv('./../data/sawonDB/deptDB.csv',
                   names=['deptno','dname','loc'],header=None)
sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',
                    names=['sabun','saname','deptno','sajob',
                           'sapay','sahire','sasex','samgr'],header=None)
gogekDB=pd.read_csv('./../data/sawonDB/gogekDB.csv',
                    names=['gobun','goname','gotel','gojumin','godam'],header=None)


deptDB['dname']=deptDB['dname'].str.strip("' ")
deptDB['loc']=deptDB['loc'].str.strip("' ")

sawonDB['saname']=sawonDB['saname'].str.strip("' ")
sawonDB['sajob']=sawonDB['sajob'].str.strip("' ")
sawonDB['sahire']=sawonDB['sahire'].str.strip("' ")
sawonDB['sasex']=sawonDB['sasex'].str.strip("' ")

gogekDB['goname']=gogekDB['goname'].str.strip("' ")
gogekDB['gotel']=gogekDB['gotel'].str.strip("' ")
gogekDB['gojumin']=gogekDB['gojumin'].str.strip("' ")


# In[7]:


deptDB


# In[8]:


sawonDB


# In[9]:


gogekDB


# ### Q3. sawonDB에서 사원번호가 짝수인 사람 출력

# In[14]:


print('사원번호가 짝수인 사원',end='\n===>')

for i in range(sawonDB['sabun'].count()):
    if int(sawonDB['sabun'][i])%2==0:
        print(sawonDB['saname'][i],end='  ')
    else:
        pass


# In[15]:


sabun_even=sawonDB[sawonDB['sabun']%2==0]
sabun_even

