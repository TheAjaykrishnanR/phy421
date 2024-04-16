def bm(func, a,b, maxiter):
    if  func(a)*func(b) < 0 and maxiter < 10:
        global p
        p = (a+b)/2
        if func(p) == 0:
            return p
        elif func(a)*func(p) < 0:
            b = p
            maxiter += 1
            return bm(func, a, b, maxiter)
        else:
            a = p
            maxiter += 1
            return bm(func, a, b, maxiter)
    else: return p

print(bm(lambda x: x**2 - 2, 1, 3, 0))
