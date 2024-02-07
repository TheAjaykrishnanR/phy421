from base import RecursiveCaller, Euler_D, RK_2, Euler_F, RK_4, CoupledRecursiveC
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)

# _, _h = RecursiveCaller(0, 100, 10, 1, 0, RK_4, lambda y, x: -0.5*y, [])
_, _h = CoupledRecursiveC(0, [100], 10, 1, 0, RK_4, [lambda y, x: -0.5*y], [], [])

print(_h)
# plt.plot(x, _h[0])
plt.show()

    
    
    