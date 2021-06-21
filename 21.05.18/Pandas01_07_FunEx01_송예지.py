
# coding: utf-8

# ## 기본 함수 선언 연습 01
# 
# <h4>기본 연습</h4>
# 
# HTML : Hyper Text Markup Language

# In[1]:


def add(a,b): # a,b는 매개변수
    return a+b

a=3
b=4
c=add(a,b) #a,b는 인수

print('%d+%d= : %d'%(a,b,c))


# ### 매개변수 지정하여 호출하기

# #### 1.일반적인 함수

# In[3]:


def add(a,b):
    return a,b,a+b

a,b,result=add(b=5,a=3)
print('%d+%d=%d'%(b,a,result))


# #### 2.입력 값이 없는 함수

# In[4]:


def say():
    return 'Hi'
print(say())


# #### 3.결과 값이 없는 함수
# 결과 값은 오직 return명령어로만 돌려받을 수 있다.

# In[5]:


def add2(a,b):
    print('%d,%d의 합은 %d입니다.'%(a,b,a+b))

print(add2(3,4))


# #### 4. 입력값도 결과값도 없는 함수

# In[7]:


def say2():
    print('Hi')
    
print(say2())

