Generate a random integer from 0 to 100:
from numpy import random
x = random.randint(100)
print(x)
Output:
12
Generate a random float from 0 to 1:
from numpy import random
x = random.rand()
print(x)
Output:
0.4039443604901367
Generate a 1-D array containing 5 random integers from 0 to 100:
from numpy import random
x=random.randint(100, size=(5))
print(x)
Output:
[15 2 78 69 47]
Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
from numpy import random
x = random.randint(100, size=(3, 5))
print(x)
Output:
[[80 54 19 74 65] 
[26 60 69 34 25] 
[50 16 53 84 90]]
Example
Generate a 1-D array containing 5 random floats:
from numpy import random
x = random.rand(5)
print(x)
Output:
[0.0717149 0.1610171 0.7472575 0.5405383 0.6102538]
Generate a 2-D array with 3 rows, each row containing 5 random numbers:
from numpy import random
x = random.rand(3, 5)
print(x)
Output:
[[0.03379952 0.78263517 0.9834899 0.47851523 0.02948659] 
[0.36284007 0.10740884 0.58485016 0.20708396 0.00969559] 
[0.88232193 0.86068608 0.75548749 0.61233486 0.06325663]]
from numpy import random
x = random.choice([3, 5, 7, 9])
print(x)
Output:
3
The choice() method also allows you to return an array of values.
Add a size parameter to specify the shape of the array.
Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
from numpy import random
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
Output:
[[9 3 5 5 7] 
[7 5 3 3 9] 
[7 5 9 9 7]]