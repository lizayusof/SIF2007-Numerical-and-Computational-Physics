import numpy as np
from scipy.linalg import cholesky


A = np.array([[14, 14, -9, 3,-5], [14, 52, -15, 2,-32], [-9, -15, 36, -5,16], [3, 2, -5, 47,49],[-5,-32,16,49,79]])
b = b = np.array([-15,-100,106,329,463])
L = cholesky(A, lower = True)
L = L @ L.T.conj()


print(print)


