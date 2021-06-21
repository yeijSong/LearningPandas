
# coding: utf-8

# In[2]:


import pandas as pd

dict_data={'a':[1,3],'b':[2,3],'c':[3,3]}
sr=pd.Series(dict_data)

print(type(sr))
print()
print(sr)


# In[3]:


list_data=[ '2021-05-19',3.14,'ABC',100,True ]
sr=pd.Series(list_data)
print(sr,'\n')


# In[5]:


idx=sr.index
val=sr.values

print('sr.index : ',idx)
print('sr.index type : ',type(idx),'\n')
print('sr.values : ',val)
print('sr.values type : ',type(val),'\n')


# In[6]:


tup_data=('영인','2010-05-01','여',True)
sr=pd.Series(tup_data, index=['이름','생년월일','성별','학생여부'])
print(sr,'\n')

print(sr[0])
print(sr['이름'])


# In[7]:


#여러 개의 원소를 선택(인덱스 리스트 활용)
print(sr[[1,2]],'\n')
print(sr[['생년월일','성별']],'\n')

#여러 개의 원소를 선택(인덱스 범위 지정)
print(sr[1:2],'\n')
print(sr['생년월일':'성별'])


# In[8]:


a=range(1,7)
print(a)

for idx in a:
    print(idx)


# In[9]:


test=sr['생년월일':'성별']
print(test)
type(test)

