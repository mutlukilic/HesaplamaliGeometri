import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

get_ipython().magic('matplotlib notebook')
n = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n) 
x = np.sin(theta)
y = np.cos(theta)
z = theta
ax.plot(x, y, z, 'b', lw=2)


theta_current = 3 * np.pi/2  
x_1=math.cos(theta_current)  
y_1=math.sin(theta_current)
z_1=1

x_2=math.sin(theta_current) 
y_2=-math.cos(theta_current)
z_2=theta_current

x_3=x_1+x_2
y_3=y_1+y_2
z_3=z_1+z_2

x_s=[x_3,x_2]
y_s=[y_3,y_2]
z_s=[z_3,z_2]

ax.plot(x_s,y_s,z_s) 
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

get_ipython().magic('matplotlib notebook')
n = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n) 
a=5
b=7
x = a*np.sin(theta)
y = b*np.cos(theta)
z = theta
ax.plot(x, y, z, 'b', lw=2)


theta_current = 3 * np.pi/2  
x_1=math.cos(theta_current)  
y_1=math.sin(theta_current)
z_1=1

x_2=a*math.sin(theta_current) 
y_2=b*-math.cos(theta_current)
z_2=theta_current

x_3=x_1+x_2
y_3=y_1+y_2
z_3=z_1+z_2

x_s=[x_3,x_2]
y_s=[y_3,y_2]
z_s=[z_3,z_2]

ax.plot(x_s,y_s,z_s)
plt.show()
