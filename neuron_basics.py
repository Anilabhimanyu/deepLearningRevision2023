import numpy as np

inputs=[1,2,3]
weights=[3,4,5]
bias=3

output=np.dot(inputs,weights)+bias
output2=inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+bias
print(output)
print(output2)