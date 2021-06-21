
# coding: utf-8

# ### 함수의 결과값은 언제나 하나이다. 
# ### 튜플값 하나인(a+b,a*b)로 돌려준다

# In[1]:


def add_and_mul(a,b):
    return a+b,a*b

result=add_and_mul(3,4)
print(result)


# ### 튜플 값을 2개의 결과값처럼 받고 싶다면,

# In[2]:


result1,result2=add_and_mul(3,4)
print(result1,result2)

