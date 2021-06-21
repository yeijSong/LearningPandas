
# coding: utf-8

# In[1]:


import pandas as pd

sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',
                    names=['sabun','saname','deptno','sajob',
                           'sapay','sahire','sasex','samgr'],header=None)

sawonDB['saname']=sawonDB['saname'].str.strip("' ")
sawonDB['sajob']=sawonDB['sajob'].str.strip("' ")
sawonDB['sahire']=sawonDB['sahire'].str.strip("' ")
sawonDB['sasex']=sawonDB['sasex'].str.strip("' ")


# In[2]:


sawonDB


# ## Q10. 입력된 이름의 연봉 출력

# In[3]:


name=input('이름을 입력하세요 : ')

sapay_name=sawonDB[sawonDB['saname']==name]
print('%3s님의 연봉은 %.2f만원입니다.'%(name,sapay_name['sapay']))


# ## Q11.사원의 소득 분류
# 이름 입력받은 후
# 해당 사원의 월급이 3000이상이면 상위소득자/
# 2000이상 3000미만 중간소득자/
# 나머지는 월급 조정 대상자

# In[4]:


name=input('이름을 입력하세요 : ')

sapay_name=sawonDB[sawonDB['saname']==name]
if (sapay_name['sapay'].item() >= 3000):
    print('"%s"님은 "상위소득자"입니다.'%(name))
elif (sapay_name['sapay'].item() < 2000):
    print('"%s"님은 "월급 조정 대상자"입니다.'%(name))
else:
    print('"%s"님은 "중간소득자"입니다.'%(name))


# ## Q12. 부서번호가 10,20인 사원들의 이름,월급,부서번호 출력

# In[5]:


sawon_10_20=sawonDB[(sawonDB['deptno']==10)|(sawonDB['deptno']==20)]
sawon_10_20[['deptno','saname','sapay']]


# ## Q13. 급여가 1000~3000사이의 직원 이름과 급여 출력

# In[6]:


grSawon=sawonDB[(sawonDB['sapay']>=1000)&(sawonDB['sapay']<3000)]
grSawon[['saname','sapay']]


# ## Q21. 입력받은 직위에 해당하는 사원들의 이름과 직위 출력
# 다만 없는 직위를 입력하면 해당 직위는 없습니다. 라는 메세지 출력

# In[23]:


job=input('직위를 입력해주세요->')
jobList=sawonDB['sajob'].unique()

if job in jobList:
    print(sawonDB[sawonDB['sajob'].isin([job])][['saname','sajob']])
else:
    print('해당 직위는 존재하지 않습니다.')


# In[20]:


sawonDB[sawonDB['sajob'].isin(['대리'])][['saname','sajob']]

