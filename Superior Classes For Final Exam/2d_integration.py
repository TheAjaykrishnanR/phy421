from integration import Integrators
import numpy as np
from typing import Callable

def xy_integrator(ax, bx, ay, by, nx, ny, f: Callable[[float, float], float]):
    y = np.linspace(ay, by, ny + 2)
    dy = (by - ay)/(ny + 1)
    result = 0
    for _y in y:
        def reduced_f(x):
            return f(x, _y)
        I = Integrators(ax, bx, nx, reduced_f)
        result += dy*I.simpsons13()
    return result

print(xy_integrator(0,2,0,1,10,10,lambda x,y:np.exp(-x*y)))