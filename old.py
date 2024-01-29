from collections.abc import Callable

'''
    A file containing all the functions that would be required in 
    the PHY 421 course. There are functions to numerically evaluate
    differential equations, algorithms to find square roots and lot
    more. Happy coding !

    Written by Ajaykrishnan R
'''
# x_0 |
# y_0 | initial state
# x  => target
# dx => step size
# y_p => first derivative
# cc => call count, always give 0 !

def Euler(x_0:float, y_0:float, x: float, dx: float, y_p: callable, cc: int) -> float:
    global y, _x, _h
    if (cc == 0):
        y = y_0
        _x = x_0
        _h = []

    if (_x >= x):
        return y, _h
    else:
        y += y_p(_x)*dx
        _x += dx
        cc += 1
        _h.append(y)
        return Euler(_x, y, x, dx, y_p, cc)


# print(Euler(0, 0, 2, 0.01, lambda x : 2*x, 0))



def RecursiveCaller(x_0:float, 
                    y_0:float, 
                    x: float,
                    dx: float, 
                    cc: int, 
                    step_func: callable, 
                    f_y: callable, 
                    *args):
    
    global y, _x, _h

    if (cc == 0):
        y = y_0
        _x = x_0
        _h = []

    if (_x >= x):
        return y, _h
    
    else:
        _h.append(y)
        y += step_func(_x, dx, f_y, y, *args)
        _x += dx
        cc += 1
        return RecursiveCaller(_x, y, x, dx, cc, step_func, f_y, *args)
    
def euler(_x: float, 
          dx: float, 
          y_p: Callable[[float], float], 
          y: float):
    
    return y_p(_x)*dx

def rk_2(_x: float, 
         dx: float, 
         f_y: Callable[[float, float], float], 
         y: float, 
         params: list[float]):
    
    al, bt, a, b = params
    k_1 = f_y(y, _x)
    k_2 = f_y(y + bt*dx*k_1, _x + al*dx)
    return (a*k_1 + b*k_2)*dx


print(RecursiveCaller(0, 0, 10, 1, 0, euler, lambda x: 2*x))
print("Stupid")
print("Stupid")
print("Stupid")
print(RecursiveCaller(0, 0, 10, 1, 0, rk_2, lambda y, x: 2*x, [0.5, 0.5, 0, 1]))
