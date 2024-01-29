from base import RecursiveCaller, Euler, RK_2
import matplotlib.pyplot as plt
import numpy as np

_x = np.arange(0, 10, 0.1)

x = np.arange(0, 10, 1)
x2 = np.arange(0, 10, 1)

_, _h = RecursiveCaller(0, 0, 10, 1, 0, Euler, lambda x: 2*x)
_, _h2 = RecursiveCaller(0, 0, 10, 1, 0, RK_2, lambda y, x: 2*x, [0.5, 0.5, 0, 1])

plt.plot(x, _h, label="Euler")
plt.plot(x2, _h2, label="RK-2")
print("x", x)
print("Euler: ",_h)
print("RK-2:", _h2)
plt.plot(_x, _x**2, label="original")
plt.legend()

plt.show()