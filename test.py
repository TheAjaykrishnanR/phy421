from base import RecursiveCaller, Euler, RK_2
import matplotlib.pyplot as plt
import numpy as np

# f(x) = x**2
x = np.arange(0, 2, 0.1)

_x = np.arange(0, 2, 0.1)
_, _h = RecursiveCaller(0, 0, 2, 0.1, 0, Euler, lambda x: 2*x)
_, _h2 = RecursiveCaller(0, 0, 2, 0.1, 0, RK_2, lambda y, x: 2*x, [0.5, 0.5, 0, 1])

print(_h)
plt.plot(x, x**2, label="Original")
plt.plot(_x, _h, label="Euler")
plt.plot(_x, _h2, label="RK 2")
plt.legend()
plt.show()

