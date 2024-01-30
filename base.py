'''
    A file containing all the functions that would be required in 
    the PHY 421 course. There are functions to numerically evaluate
    differential equations, algorithms to find square roots and lot
    more. Happy coding !

    Written by Ajaykrishnan R
'''

from collections.abc import Callable

def RecursiveCaller(
        x_0: float, 
        y_0: float, 
        x: float,
        dx: float, 
        cc: int, 
        step_func: callable, 
        f_y: callable, 
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
        y += step_func(_x, y, dx, f_y, *args)
        _x += dx
        cc += 1
        return RecursiveCaller(_x, y, x, dx, cc, step_func, f_y, *args)

# For 

def Euler_F(
        _x: float,
        y: float,
        dx: float, 
        f_y: Callable[[float], float]
        
) -> float:
    
    return f_y(_x)*dx

def RK_2(
        _x: float, 
        y: float, 
        dx: float,
        f_y: Callable[[float, float], float], 
        params: list[float]     
) -> float:
    
    al, bt, a, b = params
    k1 = f_y(y, _x)
    k2 = f_y(y + bt*dx*k1, _x + al*dx)
    return (a*k1 + b*k2)*dx

# For Solving coupled ODEs
def CoupledRecursiveC(
        x_0: float,
        l_y_0: list[float],
        x: float,
        dx: float, 
        cc: int,
        step_func: callable,
        l_f_y: list[callable],
        *args
) -> list[float]:
    
    global l_y, _x, _h 

    if (cc == 0):
        l_y = l_y_0
        _x = x_0
        _h = []
        _l_h = []

    if (_x >= x):
        return l_y, _h
    
    else:
        for y in l_y:
            _h.append(y)
            y += step_func(_x, l_y, dx, l_f_y, *args)
            _x += dx
            cc += 1

        _l_h.append(_h)
        return RecursiveCaller(_x, l_y, x, dx, cc, step_func, l_f_y, *args)
    
def Euler_D(
        _x: float,
        y: float,
        dx: float, 
        f_y: Callable[[float], float]
        
) -> float:
    
    return f_y(y)*dx