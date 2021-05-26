import numpy as np
import matplotlib.pyplot as mpl

def f(x):
    return 2.0-np.exp(x) 

def fp(x):
    return -np.exp(x)

x = 0.0
for i in range (0,10):
    xi = x - f(x)/fp(x) 
    delx = abs(xi-x)
    x = xi
    if delx > 1.0e-4:
      print(i,xi,f(x),delx)
      mpl.plot(x,f(x),'bx--')



x = np.arange(0,10,1)
mpl.title ('Newton Method for Non-Linear Equations')
mpl.xlabel('x-axis')
mpl.ylabel ('y-axis')
mpl.plot(x,f(x),'g-')



mpl.show()
