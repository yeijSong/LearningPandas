
# coding: utf-8

# In[3]:


nList=[28,31,24,25,30,32,20,30,31,26,31]
nList.sort()
print(nList)


# In[4]:


def mMean():
    m=sum(nList[0:])/len(nList)
    return m


# In[5]:


mMean()


# In[6]:


def mMedian():
    nList.sort()
    nList
    a=len(nList)
    if a%2==1:
        return nList[a//2]
    elif (a%2)==0:
        return (nList[(a//2)-1]+nList[a//2])/2


# In[7]:


mMedian()


# In[8]:


def mDeviation():
    devList=[]
    m=sum(nList[0:])/len(nList)
    for i in range(len(nList)):
        dev=nList[i]-m
        devList.append(dev)
    return devList


# In[9]:


mDeviation()


# In[10]:


def mVariance():
    devList=[]
    m=sum(nList[0:])/len(nList)
    for i in range(len(nList)):
        dev=nList[i]-m
        devList.append(dev)

    vList=[]
    for j in range(len(nList)):
        v=devList[j]**2
        vList.append(v)
    Variance=sum(vList)/(len(nList)-1)
    return Variance


# In[11]:


mVariance()


# In[12]:


def mStandardDeviation():
    devList=[]
    m=sum(nList[0:])/len(nList)
    for i in range(len(nList)):
        dev=nList[i]-m
        devList.append(dev)

    vList=[]
    for j in range(len(nList)):
        v=devList[j]**2
        vList.append(v)
    Variance=sum(vList)/(len(nList)-1)

    return Variance**(1/2)


# In[13]:


mStandardDeviation()


# In[14]:


def mRange():
    return max(nList)-min(nList)


# In[15]:


mRange()


# In[16]:


import pandas as pd

da=pd.Series(nList)
print('Built-in 정렬 sort_values() : \n', da.sort_values(ascending=True))
print('Built-in 평균 mean() : %d' %da.mean())
print('Built-in 중위수 median() : %d' %da.median())
print('Built-in 분산 var() : %d' %da.var())
print('Built-in 표준편차 std() : %d' %da.std())
print('Built-in 제1사분위수 quantile() : %d' %da.quantile(q=0.25))
print('Built-in 제2사분위수 quantile() : %d' %da.quantile(q=0.5))
print('Built-in 제3사분위수 quantile() : %d' %da.quantile(q=0.75))

da.describe()

