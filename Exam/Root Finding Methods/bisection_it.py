def f(x):
    return x**2 - 2

a, b = 1, 3
iters = 10

for i in range(0, iters):
    p = (a+b)/2
    print(p)
    if f(p) == 0:
        break
    elif f(a)*f(p) > 0:
        a = p
    else:
        b = p

