import numpy as np

x = np.array([-1.0, 1.0, 2.0])
print(x)
y = x > 0
print(y)
y = y.astype(np.int)
print(y)

# x를 bool형으로 변환 -> astype을 사용하면 bool형을 true=1 false=0으로 변환