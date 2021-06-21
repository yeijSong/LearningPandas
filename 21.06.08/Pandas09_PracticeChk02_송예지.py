
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np


# In[12]:


s=pd.Series(['1.Ant.  ', '2.Bee!\n', '3.Cat?\t',np.nan])
s


# In[13]:


s.str.strip()


# In[14]:


s.str.strip('.')


# In[15]:


s.str.strip('123.!? \n\t')


# In[16]:


s.str.lstrip('123.')


# In[17]:


s.str.rstrip('.!? \n\t')

