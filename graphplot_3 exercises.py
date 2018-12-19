#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
from matplotlib import pyplot as plt 


# In[2]:

#plotting graph for linear equation y=x+1 line

x = np.arange(11) 
y = x + 1 
plt.title("Matplotlib: y=x+1 graph") 
plt.xlabel("x axis coordinates") 
plt.ylabel("y axis coordinates") 
plt.plot(x,y) 
plt.show()


# In[3]:


y = 2 ** x  #plotting graph for equation y is equal to 2 power x 
plt.title("Matplotlib: y=2 ** x graph") 
plt.xlabel("x axis coordinates") 
plt.ylabel("y axis coordinates") 
plt.plot(x,y,'ro') #formating style if our plot-red dots
plt.show()


# In[4]:


# evenly sampled intervals
g = np.arange(0,6,0.5)
plt.title("Graph for a y=x,its sqaures,its cube")
plt.xlabel("x axis coordinates") 
plt.ylabel("y axis coordinates") 
# red dashes, blue squares and green triangles
plt.plot(g, g,'r--', g, g**2, 'bs', g, g**3, 'g^')
plt.show()

