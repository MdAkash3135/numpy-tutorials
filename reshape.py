# Reshape a 1D array to 2D (2 rows, 4 columns)
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 4)
print(newarr)
print(arr)

# Reshape a 1D array to 2D (4 rows, inferred columns)
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(4,-1)

print(newarr)

# Flatten a 2D array to 1D
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)