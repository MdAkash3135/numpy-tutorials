# Concatenate two 1D arrays
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

# Concatenate two 2D arrays along columns (axis=1)
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6, 7], [7, 8, 9]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)