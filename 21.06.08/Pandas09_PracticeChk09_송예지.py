
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

deptDB=deptDB.replace("'","",regex=True)
sawonDB=sawonDB.replace("'","",regex=True)
gogekDB=gogekDB.replace("'","",regex=True)


# In[3]:


deptDB


# In[4]:


sawonDB


# In[5]:


gogekDB


# ### Q7. sawonDB에서 전산부 직원의 평균연봉 출력

# In[6]:


deptno30=sawonDB[sawonDB['deptno']==30]
print('전산부 직원의 평균 연봉 :',deptno30['sapay'].mean())

