
# coding: utf-8

# In[46]:


nList=[28,31,24,25,30,32,20,30,31,26,31]
print(nList)


# In[47]:


def mMean():
    m=sum(nList[0:])/len(nList)
    print(m)


# In[48]:


mMean()


# In[56]:


def mMedian():
    nList.sort()
    nList
    a=len(nList)
    if a%2==1:
        print(nList[a//2])
    elif (a%2)==0:
        print((nList[(a//2)-1]+nList[a//2])/2)


# In[57]:


mMedian()

