    import numpy as np
     import matplotlib.pyplot as plt
     from mpl_toolkits.mplot3d import Axes3D
     #%matplotlib notebook
     fig=plt.figure()
     ax=Axes3D(fig)
     X=np.arange(-14,14,0.25)
     Y=np.arange(-14,14,0.25)
     X, Y=np.meshgrid(X,Y)
     #R=np.sqrt(X**2+Y**2)
     R=(X**2+Y**2)
     Z=np.sin(R)
     Z_planes=-5+2*X+4*Y
     
     ax.plot_surface(X, Y, R, rstride=1, cstride=1, cmap='hot')
     ax.plot_surface(X, Y, Z_planes, rstride=1, cstride=1, cmap='hot')
