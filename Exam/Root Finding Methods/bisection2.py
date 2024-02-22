def f(x):
    return x**2 - 2

a, b = 1, 3

for i in range(0,10):
    p = (a+b)/2
    if f(p) == 0:
        print(p)
        break
    elif f(a)*f(p) < 0:
        b = p
        print(p)
    else:
        a = p
        print(p)
