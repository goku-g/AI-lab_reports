import numpy as np
import matplotlib.pyplot as plt

def step(val):
    if val > 0:
        return 1
    else:
        return -1

def pred(X, thetas):
    sum = X[0]*thetas[0][0] + X[1]*thetas[1][0] + X[2]*thetas[2][0]
    print("sum =", sum)
    return step(sum)

x = [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1]]

y = [1, 1, 1, -1]

rand = np.random.RandomState(42)
theta = rand.uniform(size=(3, 1))*0.5

print("Theta\n", theta)

alpha = 0.1
errors = []
theta0 = []
theta1 = []
theta2 = []

for k in range(10):
    for i in range(len(x)):
        val = theta[0] + x[i][1]*theta[1] +x[i][2]*theta[2]
        y_hat = step(val)
        error = y[i] - y_hat
        errors.append(error)

        for j in range(3):
            theta[j] = theta[j] + alpha * x[i][j] * error
        
        theta0.append(theta[0])
        theta1.append(theta[1])
        theta2.append(theta[2])


fig, ax = plt.subplots(2, 2, figsize=(13, 9))
ax[0,0].plot(theta0)
ax[0,1].plot(theta1)
ax[1,0].plot(theta2)
ax[1,1].plot(errors)
plt.show()