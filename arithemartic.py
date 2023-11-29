import numpy as np
arr1 = np.arange(36).reshape(6,6)
arr2 = np.random.randint(100,size=(6,6))
print("arr1 = ",arr1)
print("arr2 = ",arr2)
print("sum = ",arr1+arr2)
print("Difference = ",arr1-arr2)
print("Multiplication = ",arr1*arr2)
print("Vector Multiplication = ",np.dot(arr1,arr2))
print("Transverse of arr1 = ",np.transpose(arr1))
print("inverse of arr1 = ",np.linalg.inv(arr1))
print("power of arr1 = ",np.linalg.matrix_power(arr1,2))
print("power of arr2 = ",arr2**2)
import numpy as np
arr = np.arange(0,150,10)
print(arr)
print(arr[1])
print(arr[2:3])
print(arr[3:8:2])
print(arr[4::3])
import numpy as np
arr = np.array([])
for i in range(12):
 arr = np.append(arr,input())
arr = arr.reshape(3,4)
print(arr)
import numpy as np
arr = np.array([])
arr = np.append(arr,[[1,2,3,4]])
print(arr)
import numpy as np
arr = np.array([])
arr = np.append(arr,[[1,2,3,4]])
print(arr)
print(arr.reshape(2,2))
import numpy as np
arr = np.array([])
for i in range(12):
 arr = np.append(arr,[1,2,3,4])
arr = arr.reshape(12,4)
print(arr)
import numpy as np
arr = np.random.randint(100,size=16)
print(arr)
print(arr[2:10:3])
arr = arr.reshape(4,4)
print(arr)
print(arr[3][2])
print(arr[3,:])
print(arr[:,2])
print(arr[1:3,2])
print(arr[3,0:2])
print(arr[0:2,1:3])
arr = arr.reshape(2,2,4)
print(arr)
print(arr[1])
print(arr[0,1,:])
print(arr[1,:,2])
print(arr[1,0,3])
import numpy as np
arr=np.random.randint(20,size=(10))
print(arr)
index_arr_1 = np.array([3,5,8])
print(arr[index_arr_1])
print(arr[arr>5])
arr = np.arange(10)
print(arr)
index_arr_1 = np.array([3,5,9])
print('The 3rd, 5th and 9th elements of the array are \n', arr[index_arr_1])
import numpy as np
arr= np.empty((8,4))
for i in range(8):
 arr[i] = i
print(arr)
arr[[4,3,0,5]]
arr[[1, 5, 7, 2], [0, 3, 1, 2]]
arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]
arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]