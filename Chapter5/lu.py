import numpy as np
from scipy.linalg import lu_factor,lu_solve

A = np.array([[9,3,2,0,7],[7,6,9,6,4],[2,7,7,8,2],[0,9,7,2,2],[7,3,6,4,3]])
b = np.array([35,58,53,37,39])

lu,piv = lu_factor(A)

x = lu_solve((lu,piv),b)

#print(lu,piv)


print(x)
