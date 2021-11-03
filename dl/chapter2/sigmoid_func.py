import matplotlib.pyplot as plt
import numpy as np


def sigmoid_func(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1., 1., 2.])

print(sigmoid_func(x))

t = np.array((1., 2., 3.))
print(1.0 + t)
print(1.0 / t)

sig_x = np.arange(-5.0, 5.0, 0.1)
sig_y = sigmoid_func(sig_x)
plt.plot(sig_x, sig_y)
plt.ylim(-.1, 1.1)
plt.show()