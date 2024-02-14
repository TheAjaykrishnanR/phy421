from math import sin as SIN, exp as EXP
A=[0]*5; G=[[0]*5]*5; W=[0]*5; X=[0]*5; W[1]=W[4]=1/6; W[2]=W[3]=1/3
def FNF(T, X1, X2, X3, X4): return -4*SIN(T)-X1-X2-X3-(4*X4)+X4*(X4-X3+X2-X1)
def FNQ(Z): return Z
print("t0,n,h,kmax"); T, N, H, KM = [float(_) for _ in input().split(",")]; N, KM = int(N), int(KM)
for I in range(1, N): print(f"INPUT D{I}(X)"); X[N-I] = float(input())
for K in range(1, KM+1): 
    print(T, X[N-1], EXP(T)+SIN(T))
    for I in range(1, 4+1):
        for J in range(1, N+1):
            P = 0.5
            if I == 1: P = 0
            if I == 4: P = 1
            if J > 1: G[I][J] = FNQ(X[J - 1])
            X[J] += H*W[I]*G[I][J]
            A[J] = X[J] + P*H*G[I][J]
        G[I][1] = FNF(T + P*H, A[1], A[2], A[3], A[4])
    T += H
        


