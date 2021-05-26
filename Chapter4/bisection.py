
# -*- coding: utf-8 -*-
#created by Norhasliza Yusof for SIF2007/SMES2105 Numerical and Computational Methods class
#created on Wed, 28 November 2018; 12.17 pm

import numpy as np
import matplotlib.pyplot as mpl


def f(x):
    return x**6-x-1.0

x = np.arange(0.0,2.0,0.1)


#print(x,f(x))

tol = 10**(-6)

a = 0.0
b = 2.0
c = a+0.5*(b-a)
delx = abs(b-a)

print("{:f} {:f} {:f} {:f} ".format(a,b,f(a),f(b)))
for i in range(0,20):
  c = a+0.5*(b-a)
  if f(c)*f(a)<0:
    a = a
    b = c
    delx = abs(b-a)
  else:
       a = c
  if delx > tol:
#    stop
   print("{:f} {:f} {:f} {:f} {:f} ".format(a,b,f(a),f(b),delx))
   mpl.plot(a,f(a),'bo')
   mpl.plot(b,f(b),'rd')
#mpl.title('Solution for bisection method:  $f(x)=x-2.0e^{-x/2}$')
#mpl.title('Your name, matrix no, bisection method')
#mpl.text(1.14351,0.040761, 'root')
#mpl.plot(a,f(a),'o')
#mpl.plot(b,f(b),'x')

mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.plot(x,f(x),'k--')
mpl.savefig('bisection.png')
mpl.show()

            
