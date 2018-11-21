#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[16]:


a=5
b=3
# plot the ellipce
x=np.linspace(-5.0,5.0,num=10000)
y=(b**2*(1-(x**2)/(a**2)))**.5  #kökünü aldık
plt.plot(x,y,color='b')
plt.plot(x,-y,color='g')
plt.show()


# In[ ]:




