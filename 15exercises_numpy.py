#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


list1 = [1,3,5,7]  
arr1 = np.array(list1) #it returns a one-dimensional array
print(arr1)


# In[3]:


list2D = [[-1,0,1],[2,4,6],[3,5,7]] #list in 2D format
arr2 = np.array(list2D)
print(arr2) #returns 2-dimensional array having 3 rows and 3 columns


# In[4]:


#ndmin specifies minimum dimensions of the resultant array 
arr3 = np.array([1, 2,3,4,5], ndmin = 3) 
print(arr3)


# In[5]:


# dtype parameter - desired data type of array
arr4 = np.array([-1,2,1], dtype = complex) #dtype as complex
print(arr4)


# In[6]:


arr5 = np.array([-1,2.5,1.2], dtype = float) #dtype as float
print(arr5)


# In[7]:


#create an array of zeros
a = np.zeros((2,3),dtype=int)
print(a)


# In[8]:


#create an array of ones
a = np.ones((2,3,4),dtype = int)
print(a)


# In[9]:


#ndarray.shape-returns a tuple consisting of array dimensions,also used to resize array
arr = np.array([[0,1,5],[3,2,1]])
print(arr.shape)


# In[10]:


#to resize the ndarray
arr.shape = (3,2)
print(arr)


# In[11]:


# reshape function to resize an array
arr = np.array([[-1,0,1],[7,3,5]])
a = arr.reshape(3,2)
print(a)


# In[12]:


#ndarray.ndim returns number of array dimensions
print(a.ndim)


# In[13]:


#array of evenly spaced number
arr6 = np.arange(26)
print(arr6)


# In[14]:


#array of evenly spaced values - step value
arr7 = np.arange(1,30,2) # array of odd numbers from 1 to 30
print(arr7)


# In[15]:


#np.itemsize- returns length of each element of array
print(arr2.itemsize) #int
print(arr4.itemsize) #complex
print(arr5.itemsize) #float


# In[16]:


# returns the current values of flags
print(arr6.flags)

