import numpy as np
val =  np.random.randint(1,20,(15,))

ar = val.reshape(3,5)
print('Array Shape:', ar.shape)
print(ar)
row_max = ar.max(axis=1).reshape(-1,1)
ar = np.where(ar == row_max, 0, ar)
print('\n',ar)