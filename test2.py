from base import RecursiveCaller, Euler_D, RK_2, Euler_F
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)

_, _h = RecursiveCaller(0, 100, 10, 1, 0, Euler_D, lambda y: -0.5*y)

plt.plot(x, _h)
plt.show()

    
    
    