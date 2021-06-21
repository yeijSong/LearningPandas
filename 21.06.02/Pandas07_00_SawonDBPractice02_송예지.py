
# coding: utf-8

# In[2]:


import pandas as pd

deptDB=pd.read_csv('./../data/sawonDB/deptDB.csv',names=['deptno','dname','loc'],header=None)
sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',names=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'],header=None)
gogekDB=pd.read_csv('./../data/sawonDB/gogekDB.csv',names=['gobun','goname','gotel','gojumin','godam'],header=None)


# In[3]:


deptDB


# In[4]:


sawonDB


# In[5]:


gogekDB


# In[6]:


deptDB2=deptDB.replace("\'",'', regex = True)
deptDB2


# In[7]:


sawonDB2=sawonDB.replace("\'",'', regex = True)
sawonDB2


# In[8]:


gogekDB2=gogekDB.replace("\'",'', regex = True)
gogekDB2


# ### Q1. sawonDB에서 입사년도가 88년도인 사원 출력

# In[9]:


print('입사년도가 88년도인 사원',end='\n===>')

for i in range(sawonDB2['sahire'].count()):
    if int(sawonDB2['sahire'][i][1:5])==1988:
        print(sawonDB2['saname'][i],end='  ')
    else:
        pass


# In[10]:


print('입사년도가 88년도인 사원 리스트')
print('-'*70)

for i in range(sawonDB2['sahire'].count()):
    if int(sawonDB2['sahire'][i][1:5])==1988:
        print(sawonDB2.iloc[[i]])
    else:
        pass


# ### Q2. sawonDB에서 4월에 입사한 사원 출력

# In[11]:


print('4월에 입사한 사원',end='\n===>')

for i in range(sawonDB2['sahire'].count()):
    if int(sawonDB2['sahire'][i][7])==4:
        print(sawonDB2['saname'][i],end='  ')
    else:
        pass


# In[12]:


print('4월에 입사한 사원 리스트')
print('-'*70)

for i in range(sawonDB2['sahire'].count()):
    if int(sawonDB2['sahire'][i][7])==4:
        print(sawonDB2.iloc[[i]])
    else:
        pass


# ### Q3. sawonDB에서 사원번호가 짝수인 사람 출력

# In[13]:


print('사원번호가 짝수인 사원',end='\n===>')

for i in range(sawonDB2['sabun'].count()):
    if int(sawonDB2['sabun'][i])%2==0:
        print(sawonDB2['saname'][i],end='  ')
    else:
        pass


# In[14]:


sabun_even=sawonDB[sawonDB['sabun']%2==0]
sabun_even


# ### Q4. sawonDB에서 직위별 급여 평균 출력

# #### < 방법1 : built-in 함수 >

# In[15]:


sawonDB.groupby('sajob')['sapay'].mean()


# #### < 방법2  >

# In[16]:


sajobList=sawonDB['sajob'].unique()

print('\t< 직급별 평균연봉 리스트 >',end='\n\n')

for a in sajobList:
    grSajob=sawonDB[sawonDB['sajob']==a]
    print('%s직급의 평균연봉 : %0.2f만원'%(a,grSajob['sapay'].mean()))
    print()


# ### Q5. sawonDB에서 직위별,성별 급여 평균 출력

# #### < 방법1 : built-in 함수 >

# In[17]:


sawonDB.groupby(['sajob','sasex'])['sapay'].mean()


# #### < 방법2 >

# In[18]:


sajobList=sawonDB['sajob'].unique()
sasexList=sawonDB['sasex'].unique()

print('< 각 직급 내 성별에 따른 평균연봉 리스트 >',end='\n\n')

for i in sajobList:
    grSajob=sawonDB[sawonDB['sajob']==i]
    print('-'*45)
    for j in sasexList:
        grSajob_sex=grSajob[grSajob['sasex']==j]
        
        print('%s직급의 %s 평균연봉 : %0.1f만원'%(i,j,grSajob_sex['sapay'].mean()))


# ### Q6. 인상급여 : SawonDB에서 급여 10%인상(인상급여 필드 추가 확인)

# In[19]:


changed_sapay=sawonDB['sapay']*1.1
changed_sapay


# In[21]:


sawonDB['changed_sapay']=changed_sapay
sawonDB


# ### Q7. sawonDB 데이터에서 전산부 직원의 평균연봉 출력

# In[29]:


'''
deptno	dname	loc
0	10	'총무부'	'서울'
1	20	'영업부'	'대전'
2	30	'전산부'	'부산'
3	40	'관리부'	'광주'
'''
#deptno=30

sawonDB.groupby('deptno')['sapay'].mean().iloc[[2]]


# In[ ]:


deptList=sawonDB['deptno'].unique


# ### Q8. 컬럼 이름순 재배치, sort_values()함수 적용

# In[31]:


sorted_sawonDB=sawonDB.sort_values('saname')
sorted_sawonDB


# ### Q9.sawonDB에서 직위가 사원과 대리인 경우 직원수가 4인 이상인 직위, 평균 급여 출력

# In[71]:


sajobList=sawonDB['sajob'].unique()
sajobList2=sajobList[3:5]

for i in sajobList2:
    grSajob=sawonDB[sawonDB['sajob']==i]
    if grSajob['sajob'].count()>=4:
        print('직원 수가 4명 이상인 직급은 %s이고 평균 급여는 %.2f만원입니다'%(i,grSajob['sapay'].mean()))
    else:
        pass


# In[55]:


for i in sajobList:
    grSajob=sawonDB[sawonDB['sajob']==i]
    print(grSajob['sajob'].count())
    print(grSajob['sapay'].mean())

