
# coding: utf-8

# In[4]:


nList=[28,31,24,25,30,32,20,30,31,26,31]
print(nList)


# In[5]:


def mMean():
    m=sum(nList[0:])/len(nList)
    print(m)


# In[6]:


mMean()


# In[7]:


def mMedian():
    nList.sort()
    nList
    a=len(nList)
    if a%2==1:
        print(nList[a//2])
    elif (a%2)==0:
        print((nList[(a//2)-1]+nList[a//2])/2)


# In[8]:


mMedian()


# In[22]:


def mDeviation():
    m=sum(nList[0:])/len(nList)
    for i in range(len(nList)):
        dev=nList[i]-m
        print(dev)


# In[23]:


mDeviation()

