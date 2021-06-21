
# coding: utf-8

# In[34]:


nList=[28,31,24,25,30,32,20,30,31,26,31]
nList.sort()
print(nList)


# In[35]:


def mMean():
    m=sum(nList[0:])/len(nList)
    print(m)


# In[36]:


mMean()


# In[37]:


def mMedian():
    nList.sort()
    nList
    a=len(nList)
    if a%2==1:
        print(nList[a//2])
    elif (a%2)==0:
        print((nList[(a//2)-1]+nList[a//2])/2)


# In[38]:


mMedian()


# In[39]:


def mDeviation():
    devList=[]
    m=sum(nList[0:])/len(nList)
    for i in range(len(nList)):
        dev=nList[i]-m
        devList.append(dev)
    print(devList)


# In[40]:


mDeviation()


# In[41]:


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
    print(vList)
    print(sum(vList))
    Variance=sum(vList)/(len(nList)-1)
    print(Variance)


# In[42]:


mVariance()


# In[50]:


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


# In[51]:


mStandardDeviation()


# In[59]:


def mRange():
    return max(nList)-min(nList)


# In[60]:


mRange()

