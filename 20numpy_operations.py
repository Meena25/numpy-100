#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([[3,1,0],[2,3,1],[4,0,2]]) #3x3 arrays
b = np.array([[10,3,9],[0,1,5],[5,12,8]])


# In[3]:


#element wise addition of a and b
a1 = np.add(a,b)
print(a1)


# In[4]:


#instead of using np.add() we can directly add both a and b
c = a + b
print(c)


# In[5]:


# sum of all elements in a
total = sum(sum(a))
print(total)


# In[6]:


#Subtraction of a and b
d = a - b
print(d)


# In[8]:


#scalar multiplication
mul = a * 5
print(mul)


# In[7]:


#to multiply both matrices a and b
m = a * b
print(m)


# In[9]:


# dot product AxB
a2 = np.dot(a,b)
print(a2)


# In[10]:


t = np.array([[2,3,4],[0,1,5]])
#transpose of the matrix t
a3 = np.transpose(t)
print(a3)


# In[11]:


# inverse of matrix a
a4 = np.linalg.inv(a)
print(a4)


# In[13]:


# power function
arr = np.array([2,4,6,8,10])
p1 = np.power(arr,2) #squaring arr
p2 = np.power(arr,3) #cube of arr
print(p1)
print(p2)


# In[14]:


# mod function - returns remainder
m1 = np.mod(arr,5)
print(m1)


# In[15]:


# amin() function
print(a)
n1 = np.amin(a,1)
print(n1)


# In[16]:


# using amax() function
n2 = np.amax(a)
print(n2)


# In[17]:


#using amax(a, axis = 0) function
n3 = np.amax(a,axis = 0)
print(n3)


# In[18]:


# using median function
med = np.median(a)
print(med)


# In[19]:


# mean operation
mean = np.mean(a)
print(mean)


# In[20]:


# computing average
avg = np.average(arr)
print(avg)


# In[21]:


#computing standard deviation
std = np.std(arr)
print(std)


# In[22]:


#computing variance
v = np.var(arr)
print(v)


# In[23]:


#sorting sort() function
arr1 = np.array([3,6,1,5,4])
st = np.sort(arr1)
print(st)

