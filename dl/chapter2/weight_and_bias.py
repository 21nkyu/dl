import numpy as np

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
wx = w*x
print(wx)
print(type(wx))
print(np.sum(wx))
print(np.sum(wx) + b)