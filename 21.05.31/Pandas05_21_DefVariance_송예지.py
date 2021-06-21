
# coding: utf-8

# In[9]:


nList=[28,31,24,25,30,32,20,30,31,26,31]
nList.sort()
print(nList)


# In[10]:


def mMean():
    m=sum(nList[0:])/len(nList)
    print(m)


# In[11]:


mMean()


# In[12]:


def mMedian():
    nList.sort()
    nList
    a=len(nList)
    if a%2==1:
        print(nList[a//2])
    elif (a%2)==0:
        print((nList[(a//2)-1]+nList[a//2])/2)


# In[13]:


mMedian()


# In[14]:


def mDeviation():
    devList=[]
    m=sum(nList[0:])/len(nList)
    for i in range(len(nList)):
        dev=nList[i]-m
        devList.append(dev)
    print(devList)


# In[15]:


mDeviation()


# In[16]:


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
    print(sum(vList)/(len(nList)-1))


# In[17]:


mVariance()

