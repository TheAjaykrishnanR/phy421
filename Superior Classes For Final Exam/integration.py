import numpy as np
from typing import Callable

class Integrators:
    
    n: int # Number of points YOU want/added BETWEEN a and b EXCLUDING a and b !

    dx: float
    x: np.array
    fx: np.array = []

    def __init__(self, a, b, n, f: Callable[[np.array],np.array]):

        self.a = a
        self.b = b
        self.n = n # n has to be odd (so that panels can be even) for simpson methods to work fully and produce correct results
        self.f = f

        self.no_of_panels = n + 1
        self.total_no_of_points = n + 2

        self.dx = (b-a)/self.no_of_panels

        self.x = np.linspace(a, b, self.total_no_of_points)

        self.fx = self.f(self.x)

    def trapezoid(self):
        result = (self.dx/2)*(self.fx[0] + self.fx[-1] + 2*np.sum(self.fx[1:-1]))
        return result
    
    def simpsons13(self):
        result = (self.dx/3)*(self.fx[0] + self.fx[-1] + 4*np.sum(self.fx[1:-1:2]) + 2*np.sum(self.fx[2:-1:2]))
        return result

    def simpsons38(self):
        result = (3*self.dx/8)*(self.fx[0] + self.fx[-1] +  3*np.sum(self.fx[1:-1:3]) + 3*np.sum(self.fx[2:-1:3]) + 2*np.sum(self.fx[3:-1:3]))
        return result
    
I = Integrators(0,np.pi,9,lambda x: np.sin(x))

print(I.trapezoid())
print(I.simpsons13())
print(I.simpsons38())