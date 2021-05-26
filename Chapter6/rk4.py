def f(x,y):
  return -2.0*x*y**2

#input
n = 4
y = 1.0
x = 0.0
h = 1.0/n

#rk4

for i in range (0,n):
  K1 = f(x,y)
  K2 = f(x+(h/2.0), y+(h/2.0)*K1)
  K3 = f(x+(h/2), y+(h/2.0)*K2)
  K4 = f(x+h, y+h*K3)
  yi = y + (h/6.0)*(K1+2*K2+2*K3+K4)
  print (yi, y, x)
