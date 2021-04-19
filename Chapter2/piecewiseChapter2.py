#Created by Dr Norhasliza Yusof for SIF2007 
#This program created based on Example 2.2 Chapter 2

#import libraries
import numpy as np
import matplotlib.pyplot as mpl

#define your function
def f(x):
    return  np.log2(x)

#set the nodes
x0 = 0.25
x1 = 0.5
x2 = 1.0

#define coefficients,c
c0 = f(x0)
c1 = f(x1)
c2 = f(x2)


#define coeffiencents,d

d0 = (c1-c0)/(x1-x0)
d1 = c2-c1/(x2-x1)


#piecewise
#note the label appear twice in the graph because mpl.plot is in the for loop
for x in np.arange(0.25,0.75,0.25): 
    q0 = c0+d0*(x-x0)
#    print(x,q0) #test your value before plotting by uncomment this section
    mpl.plot(x,q0,'yo',label='q2(x)=$4x-3$')


for x in np.arange(0.5,1.5,0.5):
    q1 = c1+d1*(x-x1)
#    print(x,q1) #test your value before plotting by uncomment this section
    mpl.plot(x,q1,'rx',markersize=14,label='q1(x)=$2x-2$')


#plot real function
mpl.xlabel('x')
mpl.ylabel('f(x)')
xx = np.arange(0.25,1.2,0.1)
mpl.plot(xx,f(xx),label='real function, $f(x)=log_2(x)$')
mpl.xlim(0.0,1.2)
mpl.legend()
mpl.show()





