#!/usr/bin/env python
# coding: utf-8

# #python performance comparison
# ##list comprehension vs for loop

# In[2]:


numbers=list(range(10))
squares=[x*x for x in numbers]
print(squares)


# In[ ]:


import timeit
numbers=list(range(10000))
def list_comprehension():
    return[x*x for x in numbers]
    def for_loop():
        result=[]
        for x in numbers:
            result.append(x*x)
            return result
            print("list comprehension time:")
            print(timeit.timeit(list_comprehension,number=1000))

            print("for loop time:")
            print(timeit.timeit(for_loop,number=1000))

# In[3]:


def square_loop(number):
    result=[]
    for x in numbers:
        result.append(x*x)
        return result

        get_ipython().run_line_magic('timeit', 'square_loop(numbers)')


# In[ ]:




