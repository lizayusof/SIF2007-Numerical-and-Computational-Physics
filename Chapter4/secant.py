import numpy as np

#function to solve
def f(x):
   return 0.5*x**2-np.sin(x)

# secant method

x0  = 0.5
x1 = 1.0
tol = 1.0e-2
f0 = f(x0)
f1 = f(x1)

for i in range (0,3):
  xx = x1 - f1*((x1-x0)/(f1-f0))
  delx = abs(xx-x1)
#  print(x0,x1,xx,f0,f1)
  if delx > tol:
     print("{:f} {:f} {:f} {:f} ".format(x0,x1,xx,delx))
     x0 = x1
     x1 = xx
   
