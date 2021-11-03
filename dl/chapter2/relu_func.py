# Recified Linear Unit : 0을 넣으면 입력을 그대로 0이하면 0을 출력하는 함수
import numpy as np


def relu_func(x):
    return np.maximum(0, x)


print(relu_func(10))
print(relu_func(0.3))
print(relu_func(-.1))