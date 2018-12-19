"""
here there are 23 exercises which is based on topics
asarray(),linspace(),logspace(),basic slicing
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#np.empty-creates uninitialized array of specified shape and dtype
#np.empty(shape, dtype, order)
arr1 = np.empty([2,3], dtype = int)
print(arr1)


# In[3]:


arr2 = np.empty([3,2], dtype = float)
print(arr2)


# In[4]:


#np.asarray(a,dtype,order)-converts python sequence into ndarray
# a-input data such as list,list of tuples,tuples etc..,
list1 = [2,4,6,8] #convert list to ndarray
arr3 = np.asarray(list1)
print(arr3)


# In[5]:


#In np.asarray, dtype is set to float
arr4 = np.asarray(list1, dtype = float)
print(arr4)


# In[6]:


#ndarray from a tuple using asarray()
tup1 = (1,3,5,7)
arr5 = np.asarray(tup1)
print(arr5)


# In[7]:


#ndarray from list of tuples using asarray()
lt = [(11,15),(20,18,25)]
arr6 = np.asarray(lt)
print(arr6)


# In[8]:


#np.linspace(start,stop,num,endpoint,retstep,dtype) -similar to arange() instead of step size number of evenly spaced values between interval is specified
arr7 = np.linspace(1,30) #default num 50 evenly spaced samples generated
print(arr7)


# In[9]:


# 8 number of evenly spaced values between 10 to 20
arr8 = np.linspace(10,20,8)
print(arr8)


# In[10]:


# endpoint is set to false (stop value 60 will not be included since endpoint is false)
arr9 = np.linspace(50,60,5,endpoint = False)
print(arr9)


# In[11]:


# to find retstep value-true-returns samples and step value
a = np.linspace(1,3,5, retstep = True)
print(a) #here retstep value is 0.5


# In[12]:


# logspace-returns numbers that are evenly spaced on a logspace
#np.logspace(start,stop,num,endpoint,base,dtype)
#start and stop endpoints of the scale are indices of the base,default-10
a1 = np.logspace(1,2,num = 10)
print(a1)


# In[13]:


# setting base of logspace to 2
a2 = np.logspace(2,11,num = 10,base = 2)
print(a2)


# In[14]:


#basic slicing - slice(start,stop,step)
#slice object is passed to extract a part of array
ar1 = np.arange(10)  #ndarray is created by arange function
s = slice(1,10,2) #starting from 1 to 9 with step of 2 is sliced
print(ar1[s])


# In[15]:


#same result is obtained when slicing parameters are separated by a colon :
ar2 = ar1[1:10:2]
print(ar2)


# In[16]:


#slicing a single item
ar3 = ar1[6]
print(ar3)


# In[17]:


#slicing items in ndarray starting from index
ar4 = ar1[4:]
print(ar4)


# In[18]:


#slicing items between 5 and 10
ar5 = ar1[5:10]
print(ar5)


# In[19]:


#slicing multi-dimensional array
ar6 = np.array([[4,5,6],[7,8,9],[10,11,12]])
print(ar6)
print(ar6[1:]) # slice array from the index a[1:]


# In[20]:


# slicing done using (...) to make selction tuple of same length as dimension of an array
# to slice the array ar6 of items in second row
print("Sliced items in second row: ",ar6[1,...])


# In[21]:


#to slice the items in second column of ar6
print("Items in second column: ",ar6[...,1])


# In[22]:


#slicing all items from column 1 onwards
print("The items from column 1 onwards: ")
print(ar6[...,1:])


# In[23]:


print("Items from row 1 onwards:")
print(ar6[1:,...])

