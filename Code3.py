import numpy as np
from numpy import linalg as LA
ma = np.array([[3, -2], [1, 0]], np.int32)
x, y = LA.eig(ma)
print('Eigenvalues of given square array:', x)
print('\nRight eigenvectors of given array:\n', y)