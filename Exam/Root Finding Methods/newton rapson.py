def f(x):
    return x**2 - 2

def fp(x):
    return 2*x

p = 1
for i in range(0, 10):
    p = p-f(p)/fp(p)
    print(p)

