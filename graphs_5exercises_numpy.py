#!/usr/bin/env python
# coding: utf-8

#Here there are 5 exercises based on topic
#sine and cosine graph,bar graphs,histogram


# In[1]:


import numpy as np 
import matplotlib.pyplot as plt  


# In[2]:


# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 5 * np.pi, 0.1) 
y = np.sin(x) 
plt.title("sine wave form") 
plt.plot(x,y)
plt.show()


# In[3]:


# cosine curve
y = np.cos(x)
plt.title("Cosine wave form") 
plt.plot(x,y)
plt.show()


# In[4]:


# plotting bar graphs
x = [2,6,8] 
y = [10,6,3]  
x2 = [3,7,9] 
y2 = [6,12,7] 
plt.bar(x, y, align = 'center') 
plt.bar(x2, y2, color = 'r', align = 'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  
plt.show()


# In[5]:


y2 = [-2,-8,-5]
plt.bar(x,y,align = 'center')
plt.bar(x2,y2,color = 'g',align = 'center')
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')
plt.show()


# In[12]:


from matplotlib import pyplot as plt 
import numpy as np  
   
a = np.array([0,1,2,3,8,5,16,35,45,32,25,37,47,43,42,13,18,24,29,10,41,49,16,19,40,11]) 
plt.hist(a, bins = [0,5,10,15,20,25,30,35,40,45,50]) 
plt.title("histogram") 
plt.show()

