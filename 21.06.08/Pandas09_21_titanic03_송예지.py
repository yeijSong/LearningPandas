
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns

titanic=sns.load_dataset('titanic')
titanic


# In[2]:


titanic.info()


# In[3]:


titanic.dtypes


# ## Q7. 연령대별 사망자수 0~10/11~20/.../70~80 ->남/녀 사망자수

# In[6]:


age0=titanic[(titanic['age']>=0)&(titanic['age']<10)]
age1=titanic[(titanic['age']>=10)&(titanic['age']<20)]
age2=titanic[(titanic['age']>=20)&(titanic['age']<30)]
age3=titanic[(titanic['age']>=30)&(titanic['age']<40)]
age4=titanic[(titanic['age']>=40)&(titanic['age']<50)]
age5=titanic[(titanic['age']>=50)&(titanic['age']<60)]
age6=titanic[(titanic['age']>=60)&(titanic['age']<70)]
age7=titanic[(titanic['age']>=70)&(titanic['age']<80)]
age8=titanic[(titanic['age']>=80)&(titanic['age']<90)]

print('10대 미만 사망자수 :',len(age0['survived']==0))
print('10대 사망자수 :',len(age1['survived']==0))
print('20대 사망자수 :',len(age2['survived']==0))
print('30대 사망자수 :',len(age3['survived']==0))
print('40대 사망자수 :',len(age4['survived']==0))
print('50대 사망자수 :',len(age5['survived']==0))
print('60대 사망자수 :',len(age6['survived']==0))
print('70대 사망자수 :',len(age7['survived']==0))
print('80대 사망자수 :',len(age8['survived']==0))


# In[4]:


print('**titanic호 연령대별 성별에 따른 사망자 수**',end='\n\n')
grAge=[]
grAgeIndex=['0~9','10~19','20~29','30~39','40~49','50~59','60~69','70~79','80~89']
for i in range(len(grAgeIndex)):
    if i < 7 :
        grAge.append(titanic[titanic['age']//10==i])
        print('%5s세 그룹 여성 사망자 수 : %3d명'
              %(grAgeIndex[i],grAge[i].groupby(['sex','survived'])['survived'].count()[0]))
        print('%5s세 그룹 남성 사망자 수 : %3d명'
              %(grAgeIndex[i],grAge[i].groupby(['sex','survived'])['survived'].count()[2]))
        print('-'*35)
    elif i==7:
        grAge.append(titanic[titanic['age']//10==i])
        print('%5s세 그룹 남성 사망자 수 : %3d명'
              %(grAgeIndex[i],grAge[i].groupby(['sex','survived'])['survived'].count()[0]))
        print('-'*35)
    else:
         print('%5s세 그룹 남성 사망자 수 : %3d명'
               %(grAgeIndex[i],0))

