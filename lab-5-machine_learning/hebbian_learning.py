import numpy as np
import matplotlib.pyplot as plt

x = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

y = [1, -1, -1, -1]

b = 1
theta  = [0, 0]

for i in range(len(x)):
    for j in range(len(theta)):
        theta[j] = theta[j] + x[i][j]*y[i]
    b = b + y[i]

print("weights : {}".format(theta))
print("bias : {}".format(b))

def activation(val):
    if(val > 0):
        return 1
    else:
        return -1

example = [-1, 1]

out = example[0]*theta[0] + example[1]*theta[1] + b

print("Output for x{} is : {}".format(example, activation(out)))