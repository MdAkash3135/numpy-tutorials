import numpy as np

arr = np.array([1.1, 2.1, 3.8])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)


arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)