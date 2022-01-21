#!/usr/bin/env python
# coding: utf-8

# In[60]:


#Ans 3
li=[4,1,8,10,15]
n=len(li)
i=min(li)
j=i+1
if j not in li:
    li.append(j)                     
            
print(li)            


# In[28]:


#And 2
def func(num,even,odd):
    if num==0:
        return
    x=num%10
    if x%2==0:
        even+=x
    else:
        odd+=x  
    print(even,odd)    
    return func(num//10,even,odd)
    
num=int(input("Enter the number:"))
y=func(num,0,0)
print(y)


# In[47]:


#Ans 1
import random
for i in ["Hello","Python","Programming","Python"]:

    guess=random.choices(l)
    print("Progress:")
    print("Guesss",guess)
    print("Address",id(guess))


# In[ ]:





# In[ ]:




