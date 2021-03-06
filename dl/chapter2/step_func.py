import numpy as np
import matplotlib.pylab as plt


def step_func(x_1: int):
    if x_1 > 0:
        return 1
    return 0


# numpy 배열을 입력으로 하기 위해서
def step_func_np(x_2: np.array):
    y_2 = x_2 > 0
    return y_2.astype(np.int)


x = np.arange(-5.0, 5.0, 1.0)
y = step_func_np(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

#3장 신경망 71p 단위계단함수