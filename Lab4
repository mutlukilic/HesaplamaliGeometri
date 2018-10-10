 #coding: utf-8

# In[31]:

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[13]:

point_test = np.array([0,0,0])
normal_test = np.array([1,-2,1]
sum(point_test*normal_test)


# In[11]:

point_test*normal_test


# In[7]:




# In[7]:

point_test*normal_test


# In[15]:

point1 = np.array([0,0,0])
normal1 = np.array([1,-2,1])


# In[16]:

point2 = np.array([0,-4,0])
normal2 = np.array([0,2,-8])
point3 = np.array([0,0,1])
normal3 = np.array([-4,5,9])


# In[27]:

d1 = -np.sum(point1*normal1)
d2 = -np.sum(point2*normal2)
d3 = -np.sum(point3*normal3)
d1,d2,d3


# In[19]:

xx, yy = np.meshgrid(range(30),range(30))


# In[20]:

xx


# In[21]:

xx, yy = np.meshgrid(range(5),range(5))
xx


# In[24]:

z1 = (-normal1[0]*xx-normal1[1]*yy-d1)*1./normal1[2]
get_ipython().magic('matplotlib inline')
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1, color='blue')


# In[22]:

yy


# In[28]:

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
point_test = np.array([0,0,0])
normal_test = np.array([1,-2,1]
d1 = -np.sum(point1*normal1)
xx, yy = np.meshgrid(range(5),range(5))
z1 = (-normal1[0]*xx-normal1[1]*yy-d1)*1./normal1[2]
%matplotlib inline
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1, color='blue')


# In[33]:

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

n = 1000
theta_max = 8*np.pi
theta = np.linspace(0,theta_max,n)
x = np.sin(theta)
y = np.cos(theta)
z = theta
ax.plot(x,y,z,'b',lw=2)


# In[ ]:
