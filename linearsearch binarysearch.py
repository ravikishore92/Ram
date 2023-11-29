Find the indexes where the value is 4:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
output:
(array([3, 5, 6]),)
Example:
Find the indexes where the values are even:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)
output:
(array([1, 3, 5, 7]),)
Example:
Find the indexes where the values are odd:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)
output:
(array([0, 2, 4, 6]),)
Find the indexes where the value 7 should be inserted:
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
output: 
1
Example:
Find the indexes where the value 7 should be inserted, starting from the right:
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)
output: 
2
To search for more than one value, use an array with the specified values.
Example:
Find the indexes where the values 2, 4, and 6 should be inserted:
import numpy as np
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
output: 
[1 2 3]