import numpy as np

inputs=[1,2,3]

weights_list=[
    [0.2,0.3,0.4],
    [0.3,0.4,0.9],
    [0.1,0.3,0.8]
]
bias=[3,4,5]
output_list=[]

print(zip(weights_list,bias))
for each_weights,each_bias in zip(weights_list,bias):
    output_of_each_neuron=0
    for i,j in zip(inputs,each_weights):
        output_of_each_neuron+=i*j
    output_of_each_neuron+=each_bias
    output_list.append(output_of_each_neuron)
print("output_list  ",output_list)

    

        