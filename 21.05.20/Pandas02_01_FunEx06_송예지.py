
# coding: utf-8

# ### return문을 2번 사용하면, 두 번째 return문은 실행되지 않는다

# In[1]:


def add_and_mul(a,b):
    return a+b
    return a*b

result=add_and_mul(2,3)
print(result)


# ### retun을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.

# In[2]:


def say_nick(nick):
    if nick=='바보':
        return
    print('나의 별명은 %s입니다'%nick)
    
say_nick('야호')
say_nick('바보')

