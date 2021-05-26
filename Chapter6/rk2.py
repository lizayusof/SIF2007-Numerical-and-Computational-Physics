#program rk2

import numpy as np
import math
import matplotlib.pyplot as mpl


def f(x,y):
    return 1.0-y

def exact(x):
  return 1.0-np.exp(-x)

n= 5
h = 1/n
y = 0.0
x = 0.0

for i in np.arange(0,n+1):
   K1 = f(x,y)
   K2 = f(x+h, y+h*f(x,y))
   yi = y + h/2.0*(K1+K2)
   print (i,x,y,exact(x))    
   x = x + h
   y = yi
   mpl.plot(x,y,'kd-')

xnew = np.arange(0,1.5,0.1)
ynew = exact(xnew)
mpl.plot(xnew,ynew)

#   mpl.plot(x,yx,'-')
mpl.show()
