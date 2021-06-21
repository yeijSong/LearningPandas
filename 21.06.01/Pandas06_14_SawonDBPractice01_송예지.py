
# coding: utf-8

# In[43]:


import pandas as pd

deptDB=pd.read_csv('./../data/sawonDB/deptDB.csv',names=['deptno','dname','loc'],header=None)
sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',names=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'],header=None)
gogekDB=pd.read_csv('./../data/sawonDB/gogekDB.csv',names=['gobun','goname','gotel','gojumin','godam'],header=None)


# In[44]:


deptDB


# In[45]:


sawonDB


# In[46]:


gogekDB


# In[47]:


deptDB2=deptDB.replace("\'",'', regex = True)
deptDB2


# In[48]:


sawonDB2=sawonDB.replace("\'",'', regex = True)
sawonDB2


# In[49]:


gogekDB2=gogekDB.replace("\'",'', regex = True)
gogekDB2


# ### Q1. sawonDB에서 입사년도가 88년도인 사원 출력

# In[102]:


print('입사년도가 88년도인 사원',end='\n===>')

for i in range(sawonDB2['sahire'].count()):
    if int(sawonDB2['sahire'][i][1:5])==1988:
        print(sawonDB2['saname'][i],end='  ')
    else:
        pass


# In[124]:


print('입사년도가 88년도인 사원 리스트')
print('-'*70)

for i in range(sawonDB2['sahire'].count()):
    if int(sawonDB2['sahire'][i][1:5])==1988:
        print(sawonDB2.iloc[[i]])
    else:
        pass


# ### Q2. sawonDB에서 4월에 입사한 사원 출력

# In[103]:


print('4월에 입사한 사원',end='\n===>')

for i in range(sawonDB2['sahire'].count()):
    if int(sawonDB2['sahire'][i][7])==4:
        print(sawonDB2['saname'][i],end='  ')
    else:
        pass


# In[126]:


print('4월에 입사한 사원 리스트')
print('-'*70)

for i in range(sawonDB2['sahire'].count()):
    if int(sawonDB2['sahire'][i][7])==4:
        print(sawonDB2.iloc[[i]])
    else:
        pass


# ### Q3. sawonDB에서 사원번호가 짝수인 사람 출력

# In[104]:


print('사원번호가 짝수인 사원',end='\n===>')

for i in range(sawonDB2['sabun'].count()):
    if int(sawonDB2['sabun'][i])%2==0:
        print(sawonDB2['saname'][i],end='  ')
    else:
        pass


# In[107]:


sabun_even=sawonDB[sawonDB['sabun']%2==0]
sabun_even


# ### Q4. sawonDB에서 직위별 급여 평균 출력

# #### < 방법1 : built-in 함수 >

# In[53]:


sawonDB.groupby('sajob')['sapay'].mean()


# #### < 방법2  >

# In[92]:


sajobList=sawonDB['sajob'].unique()

print('\t< 직급별 평균연봉 리스트 >',end='\n\n')

for a in sajobList:
    grSajob=sawonDB[sawonDB['sajob']==a]
    print('%s직급의 평균연봉 : %0.2f만원'%(a,grSajob['sapay'].mean()))
    print()


# ### Q5. sawonDB에서 직위별,성별 급여 평균 출력

# #### < 방법1 : built-in 함수 >

# In[54]:


sawonDB.groupby(['sajob','sasex'])['sapay'].mean()


# #### < 방법2 >

# In[87]:


sajobList=sawonDB['sajob'].unique()
sasexList=sawonDB['sasex'].unique()

print('< 각 직급 내 성별에 따른 평균연봉 리스트 >',end='\n\n')

for i in sajobList:
    grSajob=sawonDB[sawonDB['sajob']==i]
    print('-'*45)
    for j in sasexList:
        grSajob_sex=grSajob[grSajob['sasex']==j]
        
        print('%s직급의 %s 평균연봉 : %0.1f만원'%(i,j,grSajob_sex['sapay'].mean()))

