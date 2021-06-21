
# coding: utf-8

# In[11]:


import pandas as pd

sawonDB=pd.read_csv('./../data/sawonDB/sawonDB.csv',
                    names=['sabun','saname','deptno','sajob',
                           'sapay','sahire','sasex','samgr'],header=None)

sawonDB['saname']=sawonDB['saname'].str.strip("' ")
sawonDB['sajob']=sawonDB['sajob'].str.strip("' ")
sawonDB['sahire']=sawonDB['sahire'].str.strip("' ")
sawonDB['sasex']=sawonDB['sasex'].str.strip("' ")


# In[12]:


sawonDB


# ## Q10. 입력된 이름의 연봉 출력

# In[13]:


name=input('이름을 입력하세요 : ')

sapay_name=sawonDB[sawonDB['saname']==name]
print('%3s님의 연봉은 %4d만원입니다.'%(name,sapay_name['sapay']))


# ## Q11.사원의 소득 분류
# 이름 입력받은 후
# 해당 사원의 월급이 3000이상이면 상위소득자/
# 2000이상 3000미만 중간소득자/
# 나머지는 월급 조정 대상자

# In[21]:


name=input('이름을 입력하세요 : ')

sapay_name=sawonDB[sawonDB['saname']==name]
if (sapay_name['sapay'].item() >= 3000):
    print('"%s"님은 "상위소득자"입니다.'%(name))
elif (sapay_name['sapay'].item() < 2000):
    print('"%s"님은 "월급 조정 대상자"입니다.'%(name))
else:
    print('"%s"님은 "중간소득자"입니다.'%(name))

