import numpy as np

inputs=[1,2,3]
weights1=[0.2,0.3,0.4]
weights2=[0.3,0.4,0.9]
weights3=[0.1,0.3,0.8]

bias=3

output=np.dot(inputs,weights1)+bias
outputs=[inputs[0]*weights1[0]+inputs[1]*weights1[1]+inputs[2]*weights1[2]+bias,
inputs[0]*weights2[0]+inputs[1]*weights2[1]+inputs[2]*weights2[2]+bias,
inputs[0]*weights3[0]+inputs[1]*weights3[1]+inputs[2]*weights3[2]+bias]

print(output)
print(outputs)