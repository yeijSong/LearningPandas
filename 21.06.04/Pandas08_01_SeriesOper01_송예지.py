
# coding: utf-8

# ### 1.21_Series to number

# In[8]:


import pandas as pd

student1=pd.Series({'국어':100,'영어':80,'수학':90})
print(student1,'\n')


# In[9]:


percentage=student1/200

print(percentage,'\n')
print(type(percentage))


# ### 1.22 Series to Series

# In[3]:


import pandas as pd

student1=pd.Series({'국어':100,'영어':80,'수학':90})
student2=pd.Series({'수학':80,'국어':90,'영어':80})

print('student1',student1,'\n')
print(student2,'\n')


# In[4]:


addition=student1+student2
subtraction=student1-student2
multiplication=student1*student2
division=student1/student2

print(type(division))


# In[5]:


result=pd.DataFrame([addition,subtraction,multiplication,division],
                   index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result,'\n',type(result))


# In[7]:


print(addition,'\n\n',subtraction,'\n\n',multiplication,'\n\n',division)

