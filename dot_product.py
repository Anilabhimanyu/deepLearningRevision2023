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


import numpy as np
inputs=[1,2,3,4]
weights_list=[
    [0.2,0.3,0.4,0.5],
    [0.3,0.4,0.9,0.1],
    [0.1,0.3,0.8,0.2]
]
bias=[3,4,5]
print(np.dot(weights_list,inputs))
output=np.dot(weights_list,inputs)+bias
print(output)


"""
print(np.dot(inputs,weights_list))
output=np.dot(inputs,weights_list)+bias

Here it will raise error of
ValueError: shapes (4,) and (3,4) not aligned: 4 (dim 0) != 3 (dim 0)

because, we need to consider as the rows of weights as the no. of neurons in each layer
"""
