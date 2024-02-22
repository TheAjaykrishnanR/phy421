def bm(func, a,b): 
    if func(a)*func(b) < 0:
        p = (a+b)/2
        if func(p) == 0:
            return p
        elif func(a)*func(p) < 0:
            b = p
            return bm(func, a, b)
        else:
            a = p
            return bm(func, a, b)


print(bm(lambda x: x**2 - 2, 1, 3, 0))
