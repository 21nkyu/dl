import numpy as np


def or_func(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w)+b
    if tmp <= 0:
        return 0
    return 1