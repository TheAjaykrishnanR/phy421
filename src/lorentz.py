import numpy as np 
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 15


h = 0.01
t_final = 10
time = np.arange(0,t_final,h)
sigma = 10 
r = 28
b = 8/3

# r1 = 0,0,0
# r2 = [np.sqrt(b*(r-1)),  np.sqrt(b*(r-1)),  r-1]
# r3 = [-np.sqrt(b*(r-1)), -np.sqrt(b*(r-1)), r-1]

rc = sigma*(sigma+ b+3)/(sigma-b-1)


def sys(vars):
    x = vars[0]
    y = vars[1]
    z = vars[2]
    # specify the equations for decay chain 
    x_dot = sigma*(y-x)
    y_dot = r*x - y - x*z
    z_dot = -b*z + x*y
    vars_dot = np.array([x_dot, y_dot, z_dot])
    return vars_dot 

# Solver function for system of ODEs 
def RK4(X):
    k1 = sys(X)
    k2 = sys(X + k1*h/2)
    k3 = sys(X + k2*h/2)
    k4 = sys(X + k3*h)
    X = X + (h/6)*(k1 + 2*k2 + 2*k3 + k4) 
    return X   



data = np.zeros((len(time),3))
# specify the initial conditions
data[0,:] = [ 10, 1, 3]


# time evolution of system
for t in range(len(time)-1):
    data[t+1,:] = RK4(data[t,:])


x = data[:,0]
y = data[:,1]
z = data[:,2]

fig = plt.figure(figsize=(10,10))
plt.axes(projection='3d')
plt.title(r"$r={r},\sigma={sigma},b={b}, r_c={rc}$".format(r=r,sigma=np.round(sigma,2),b=np.round(b,2),rc=np.round(rc,2)))
plt.plot(x,y,z,color='m',alpha=0.8,lw=2)

# show the fixed points
plt.plot(0,0,0,'r*',ms=20,label='C0')
plt.plot(np.sqrt(b*(r-1)),  np.sqrt(b*(r-1)),  r-1,'b*',ms=20,label='C+')
plt.plot(-np.sqrt(b*(r-1)),  -np.sqrt(b*(r-1)),  r-1,'g*',ms=20,label='C-')
plt.plot(x[0],y[0],z[0],'ko',ms=10,label='inital state')
plt.legend()
plt.show()