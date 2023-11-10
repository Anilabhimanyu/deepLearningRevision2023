# object that can be represented as arrays is called Tensor

# 1D array
import numpy as np

arr1=np.array([1,2,3,4])
print(arr1.shape)

arr2=np.array([
    [1,2,3,4],
    [3,4,5,6]
])
print(arr2.shape)

arr3=np.array([
    [
        [1,2,3,4],
        [3,4,5,6]
    ],
    [
        [3,4,6,7],
        [5,6,4,3]
    ]
])
print(arr3.shape)