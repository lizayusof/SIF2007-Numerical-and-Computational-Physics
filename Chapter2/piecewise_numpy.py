#Example of using numpy.piecewise for piecewise interpolation
#Might need further modification to get better accuracy

#import library
from scipy import optimize
import matplotlib.pyplot as mpl
import numpy as np

def f(x):
  return np.log2(x)


x = np.array([0.25,0.5,0.75,1.0], dtype=float)

#calling piecewise.numpy, need to supply function, condition list  

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

#optimise the curve
p , e = optimize.curve_fit(piecewise_linear, x, f(x))


#for x range 0.25 to 0.5
xd = np.linspace(0.25, 0.5, 2)
mpl.plot(xd, piecewise_linear(xd, *p),'x')

#for x range 0.5 to 1.0
xx = np.linspace(0.5, 1.0, 2)
mpl.plot(xx, piecewise_linear(xx, *p),'o')

#plot the real function
mpl.plot(x, f(x), "-")


mpl.show()
