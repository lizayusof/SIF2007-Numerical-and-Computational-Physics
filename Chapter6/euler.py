import numpy as np
import math as mt
import matplotlib.pyplot as mpl

def f(t,y):
    return 1.0+y**2

t = 0.0
y = 1.0
h = 0.05
for i in range (0,11):
    yi = y + h*f(t,y)
#    t = t + h
    y = yi
    print (i,"{0:4f}".format(t),"{0:4f}" .format(yi))
    t = t+h
    mpl.plot(t,yi,'bx--')
#    mpl.ylim(0.0,1.0)
#    mpl.xlim(0.4,0.75)

x = np.arange(0,100,10)
#mpl.title ('Newton Method for Optimisation')
#mpl.xlabel('x-axis')
#mpl.ylabel ('y-axis')
#mpl.plot(x,f(x),'go-')

mpl.show()
