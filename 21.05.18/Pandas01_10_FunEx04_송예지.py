
# coding: utf-8

# ## **는 딕셔너리로 만들어져서 출력
# key=value 형태의 결과값이 그 딕셔너리에 저장됨

# In[1]:


def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(a=1)
print_kwargs(name='foo',age=3)

