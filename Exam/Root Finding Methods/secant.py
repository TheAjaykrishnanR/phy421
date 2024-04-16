def f(x):
    return x**2 - 2

def fp(x):
    return 2*x

_p = 0.75
p = 1
for i in range(0, 10):
    if fp(p) - fp(_p) != 0:
        _temp = p
        p = p-f(p)*(p - _p)/(fp(p) - fp(_p))
        _p = _temp
        print(p)

