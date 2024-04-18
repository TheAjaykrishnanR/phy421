'''
SHOOTING METHOD FOR BVP
d2y/dt2 = -g

y -> y0
y1 -> y'
t -> x

y0' = y1
y1' = -g
init : x = 0, y0 = 0, y1 = ?, y0(5) = 50
'''

from ultimate import NODES

def error(y1):
    nodes = NODES(2, 0.1, 50, {"x":0, "y0":0, "y1":y1}, {"y0":"y1", "y1":"-9.8"})
    computed = nodes.state_history["rk4"]["y0"][-1]
    actual = 50
    error = computed - actual
    return error

# print(error(25))

# finds the root of f; a and b such that f(a) < 0 and f(b) > 0
def bisection_root_finder(f: callable, a: float, b: float, tolerance: float):
    root = (a + b)/2
    while f(root) > tolerance:
        if f(a)*f(root) > 0:
            a = root
        else:
            b = root
    return root

print(bisection_root_finder(error, 25, 40, 5))