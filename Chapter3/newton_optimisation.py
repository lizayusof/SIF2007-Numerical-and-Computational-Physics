#Created by Dr Norhasliza Yusof for SIF2007 Numerical and Computational Methods lecture
#In this code, it shows how to solve optimisation using Newton's Method 
#Please refer to your lecture for the full Newton's Method equations
#In this code, all the values are in scalar 

#import numpy for numerical library
import numpy as np
import math as mt

#import matplotlib.pyplot for plotting/visualization
import matplotlib.pyplot as mpl

# insert your function f(x)
def f(x):
    return 3.0*x**3-10.0*x**2-56.0*x+5.0

#insert your function f'(x)
def fp(x):
    return 9.0*x**2-20.0*x-56.0

#insert your function f"(x)
def fpp(x):
    return 18.0*x-20.0

#intial guess
x = 2.0

#start iteration, we iterate from 0 until desirable iteration (in this case 100).
#The value of iteration can be changed to test the convergence.

for i in range (0,100):
    xi = x - fp(x)/fpp(x) #Newton's Method for optimisation
    delx = abs(xi-x)  #find the difference/error
    # to stop the iteration, we test limit of the error here, the limit is 0.001
    if delx < 10**(-5):
       print ('stop calculation')
    else:
       print(i,x,xi,delx) #if the condition fullfil, display the output
       mpl.plot(x,f(x),'ko--') #plot the points
    x = xi #update the value of x for next iteration

#plotting routine

#set the range of x-axis
x = np.arange(-4,6,0.5)

# Display title for the plot
mpl.title ('Newton Method for Optimisation $3x^3-10x^2-56x+5$')

#Display the label of the plot
mpl.xlabel('x')
mpl.ylabel ('f(x)')

#Result of the plot in the analytical form
mpl.plot(x,f(x),'g-')
#mpl.plot(x,f(x),'ko')
mpl.savefig('Chapter3.png')

#Display your result on your screen
mpl.show()
