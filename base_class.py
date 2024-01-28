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
    global y, _x
    if (cc == 0):
        y = y_0
        _x = x_0

    if (_x >= x):
        return y
    else:
        y += y_p(_x)*dx
        _x += dx
        cc += 1
        return Euler(_x, y, x, dx, y_p, cc)


def sq_p(x):
    return 2*x

print(Euler(0, 0, 2, 0.01, sq_p, 0))

