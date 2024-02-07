'''
    A file containing all the functions that would be required in 
    the PHY 421 course. There are functions to numerically evaluate
    differential equations, algorithms to find square roots and lot
    more. Happy coding !

    Written by Ajaykrishnan R
'''
from inspect import getfullargspec
from collections.abc import Callable

def RecursiveCaller(
        x_0: float, 
        y_0: float, 
        x: float,
        dx: float, 
        cc: int, 
        step_func: callable, 
        y_p: callable, 
        *args
) -> float:
    
    global y, _x, _h 

    if (cc == 0):
        y = y_0
        _x = x_0
        _h = []

    if (_x >= x):
        return y, _h
    
    else:
        _h.append(y)
        y += step_func(_x, y, dx, y_p, *args)
        _x += dx
        cc += 1
        return RecursiveCaller(_x, y, x, dx, cc, step_func, y_p, *args)

# For 

def Euler_F(
        _x: float,
        y: float,
        dx: float, 
        y_p: Callable[[float], float]
        
) -> float:
    
    return y_p(_x)*dx

def RK_2(
        _x: float, 
        y: float, 
        dx: float,
        y_p: Callable[[float, float], float], 
        params: list[float]     
) -> float:
    
    al, bt, a, b = params
    k1 = y_p(y, _x)
    k2 = y_p(y + bt*dx*k1, _x + al*dx)
    return (a*k1 + b*k2)*dx

# For Solving coupled ODEs
def CoupledRecursiveC(
        x_0: float,
        l_y_0: list[float],
        x: list[float],
        dx: float, 
        cc: int,
        step_func: callable,
        l_y_p: list[callable],
        *args
) -> list[float]:
    
    if len(l_y_p) != len(l_y_0):
        raise Exception("number of equations and init variables must be the same !")

    global l_y, _x, _l_h

    if (cc == 0):
        
        for l_y_0_v in l_y_0:
            l_y.append(l_y_0_v)
        _x = x_0
        _h = []
        _l_h = []

    if (_x >= x):
        return l_y, _l_h
    
    else:
        for idx, y in enumerate(l_y):
            _h.append(y)
            y += step_func(_x, y, dx, l_y_p[idx], *args)
            _x += dx
            cc += 1

        _l_h.append(_h)
        return RecursiveCaller(_x, l_y, x, dx, cc, step_func, l_y_p, *args)
    
def Euler_D(
        _x: float,
        y: float,
        dx: float, 
        y_p: Callable[[float], float]
        
) -> float:
    
    return y_p(y)*dx

def RK_4(
        _x: float, 
        y: float, 
        dx: float,
        y_p: callable, 
        params: list[int]
):
    k1 = y_p(y, _x)
    k2 = y_p(y + dx*k1/2, _x + dx/2)
    k3 = y_p(y + dx*k2/2, _x + dx/2)
    k4 = y_p(y + dx*k3, _x + dx)

    return (k1 + 2*k2 + 2*k3 + k4)*dx/6