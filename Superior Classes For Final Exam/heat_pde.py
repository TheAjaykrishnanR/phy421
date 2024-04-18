import numpy as np

class PDE_HEAT:  
    
    nx: int # no of x points YOU add BETWEEN a and b excluding a and b

    def __init__(self, a, b, nx, t_final, sigma, D, boundary_conds: list[callable]):

        self.a = a
        self.b = b
        self.nx = nx
        self.t_final = t_final
        self.sigma = sigma
        self.D = D
        self.boundary_conds = boundary_conds

        self.no_of_panels_x = nx + 1
        self.total_no_of_points_x = nx + 2

        self.dx = (self.b - self.a)/self.no_of_panels_x
        self.dt = (sigma/D)*self.dx**2

        self.x = np.linspace(a, b, self.total_no_of_points_x)
        self.t = np.arange(0, t_final, self.dt)

        self.total_no_of_points_t = len(self.t)

        self.x_t0, self.t_xa, self.t_xb = boundary_conds

    def createW(self):

        W = np.zeros((self.total_no_of_points_t, self.total_no_of_points_x))
        W[0,1:-1] = self.x_t0(np.linspace(self.a, self.b, self.nx))
        W[:,0] = self.t_xa(self.t)
        W[:,-1] = self.t_xb(self.t)

        return W

    def createForwardA(self):

        m = self.total_no_of_points_x
        A = np.zeros((m, m))

        j_ind_low = np.arange(0, m - 2, 1)
        i_ind = np.arange(1, m - 1, 1)
        j_ind_high = np.arange(2, m, 1)

        A[0,0] = A[-1,-1] = 1
        A[i_ind, j_ind_low ] = self.sigma
        A[i_ind, i_ind] = 1 - 2*self.sigma
        A[i_ind, j_ind_high] = self.sigma

        return A

    def createBackwardA(self):

        m = self.total_no_of_points_x
        A = np.zeros((m, m))

        j_ind_low = np.arange(0, m - 2, 1)
        i_ind = np.arange(1, m - 1, 1)
        j_ind_high = np.arange(2, m, 1)

        A[0,0] = A[-1,-1] = 1
        A[i_ind, j_ind_low ] = -self.sigma
        A[i_ind, i_ind] = 1 + 2*self.sigma
        A[i_ind, j_ind_high] = -self.sigma

        return A
    
    def forward(self):

        W = self.createW()
        A = self.createForwardA()

        for i in range(0, self.total_no_of_points_t - 1):
            W[i+1,:] = A@W[i,:]

        return W
            

    def backward(self):
        
        W = self.createW()
        A = self.createBackwardA()
        A_inv = np.linalg.inv(A)

        for i in range(0, self.total_no_of_points_t - 1):
            W[i+1,:] = A_inv@W[i,:]

        return W

abc = PDE_HEAT(0, 1, 48, 0.1, 1/3, 1, [lambda x: np.square(np.sin(2*np.pi*x)), \
                                     lambda x: 0, lambda x:0])

W = abc.forward()

import matplotlib.pyplot as plt

xx, tt = np.meshgrid(abc.x, abc.t)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(xx,tt,W,cmap='plasma')
plt.show() 

