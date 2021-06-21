
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

deptDB=deptDB.replace("'","",regex=True)
sawonDB=sawonDB.replace("'","",regex=True)
gogekDB=gogekDB.replace("'","",regex=True)


# In[2]:


deptDB


# In[3]:


sawonDB


# In[4]:


gogekDB


# ### Q1. sawonDB에서 입사년도가 88년도인 사원 출력

# In[5]:


print('입사년도가 88년도인 사원',end='\n===>')

for i in range(sawonDB['sahire'].count()):
    if int(sawonDB['sahire'][i][1:5])==1988:
        print(sawonDB['saname'][i],end='  ')
    else:
        pass


# In[6]:


print('입사년도가 88년도인 사원 리스트')
print('-'*70)

for i in range(sawonDB['sahire'].count()):
    if int(sawonDB['sahire'][i][1:5])==1988:
        print(sawonDB.iloc[[i]])
    else:
        pass


# In[29]:


sahire_1988=sawonDB[sawonDB['sahire'].str.contains('1988')]
sahire_1988


# ### Q2. sawonDB에서 4월에 입사한 사원 출력

# In[8]:


print('4월에 입사한 사원',end='\n===>')

for i in range(sawonDB['sahire'].count()):
    if int(sawonDB['sahire'][i][7])==4:
        print(sawonDB['saname'][i],end='  ')
    else:
        pass


# In[9]:


print('4월에 입사한 사원 리스트')
print('-'*70)

for i in range(sawonDB['sahire'].count()):
    if int(sawonDB['sahire'][i][7])==4:
        print(sawonDB.iloc[[i]])
    else:
        pass


# In[30]:


sahire_April=sawonDB[sawonDB['sahire'].str.contains('/04/')]
sahire_April


# ### Q3. sawonDB에서 사원번호가 짝수인 사람 출력

# In[10]:


print('사원번호가 짝수인 사원',end='\n===>')

for i in range(sawonDB['sabun'].count()):
    if int(sawonDB['sabun'][i])%2==0:
        print(sawonDB['saname'][i],end='  ')
    else:
        pass


# In[11]:


sabun_even=sawonDB[sawonDB['sabun']%2==0]
sabun_even


# In[33]:


sabunEvenList=[]
for i,value in enumerate(sawonDB['sabun']) :
    if value%2==0:
        sabunEvenList.append(i)
print(sawonDB.iloc[sabunEvenList])

