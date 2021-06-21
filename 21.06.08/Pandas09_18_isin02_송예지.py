
# coding: utf-8

# ## pd.Series.isin

# In[3]:


import pandas as pd

deptDB=pd.read_csv('./../data/sawonDB/deptDB.csv',
                   names=['deptno','dname','loc'],header=None)
sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',
                    names=['sabun','saname','deptno','sajob',
                           'sapay','sahire','sasex','samgr'],header=None)
gogekDB=pd.read_csv('./../data/sawonDB/gogekDB.csv',
                    names=['gobun','goname','gotel','gojumin','godam'],header=None)


# In[4]:


deptDB['dname']=deptDB['dname'].str.strip("' ")
deptDB['loc']=deptDB['loc'].str.strip("' ")

sawonDB['saname']=sawonDB['saname'].str.strip("' ")
sawonDB['sajob']=sawonDB['sajob'].str.strip("' ")
sawonDB['sahire']=sawonDB['sahire'].str.strip("' ")
sawonDB['sasex']=sawonDB['sasex'].str.strip("' ")

gogekDB['goname']=gogekDB['goname'].str.strip("' ")
gogekDB['gotel']=gogekDB['gotel'].str.strip("' ")
gogekDB['gojumin']=gogekDB['gojumin'].str.strip("' ")


# In[10]:


sajobChk=sawonDB[sawonDB['sajob'].isin(['대리','사원'])]
sajobCntChk=sajobChk.groupby(['sajob'])['sabun'].count()>=4
sajobChkResult=sajobCntChk[sajobCntChk.values]

for i, value in enumerate(sajobChkResult.index):
    cal=sawonDB[sawonDB['sajob']==value]
    print(cal.groupby('sajob')['sapay'].mean())


# In[9]:


sawonDB[sawonDB['sajob'].isin(['대리','사원'])]

