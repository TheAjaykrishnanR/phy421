import re
from sympy import sympify
import matplotlib.pyplot as plt
from math import sqrt

class NODES:

    '''
    NODES: NUMERICAL ORDINARY DIFFERENTIAL EQUATION SOLVER
    -------------------------------------------------------
    AUTHOR: AJAYKRISHNAN R
    -------------------------------------------------------
    '''
    N: int # No of variables / no of coupled equations 
    dx: float
    state: dict = {}
    evolvers:dict = {}
    historyx: list[float]
    historyy: list[float]


    def __init__(self, state: dict, evolvers: dict, iterations: int):

        self.dx = 0.1

        self.state = state
        self.evolvers = evolvers

        for yn in self.evolvers:
            self.evolvers[yn] = sympify(self.evolvers[yn])

        '''Run'''
        self.historyx = []
        self.historyy = []
        for i in range(0, iterations):
            self.historyx.append(self.state["y0"])
            self.historyy.append(self.state["y2"])
            self.rk4()
            print(f"iteration {i} complete")

    def rk4(self):

        _temp = {}

        G1 = {}
        G2 = {}
        G3 = {}
        G4 = {}
        Gs = [G1, G2, G3, G4]

        '''copy the state into temp and shift it for Gi calculation'''
        for idx, Gi in enumerate(Gs):
            if idx == 0: 
                Gsw = 0
                _temp = {k:v for k,v in self.state.items() if k != "x"}
            else:
                Gsw = 0.5
                if idx == 4: Gsw = 1
                _temp = {k:v + Gsw*Gs[idx - 1][k]*(self.dx) for k,v in self.state.items() if k != "x"}
            _temp["x"] = self.state["x"] + Gsw*self.dx
        
        # Calculate Gis from the updated _temp
            for yn in self.state:
                if yn != "x":
                    Gi[yn] = self.evolvers[yn].evalf(subs=_temp)
                

        '''update the state into the next step'''
        for yn in self.state:
            if yn == "x":
                self.state[yn] += self.dx
            else:
                self.state[yn]+=(self.dx/6)*(Gs[0][yn] + 2*Gs[1][yn] + 2*Gs[2][yn] + Gs[3][yn])
# -----------------------------------------------------------------------------------
    '''
    Format for filling the evolver dict:
    yN = f(x, y0, y1, ..., yN-1) where y{i} denotes the i-th 
    derivative of y with respect to x. 

    An evolver for a variable y_k is its derivative expressed as functions of the 
    implicit variable x and other STRICTLY FIRST ORDER variables y_i where i runs 
    0 to N without including k ofcourse and it calculates its value in the next state step
    using the current state as its inputs
    '''
# -----------------------------------------------------------------------------------
state = {'x':0, 'y0': 0, 'y1': 100*sqrt(3)/2, "y2": 0, "y3":50}
qd_evolvers = {'y0': "y1", 
            'y1': "-0.001834*pi*((1-0.0000238*y0)^(2.5))*(1+(1.5/(exp(sqrt(y1^2+y3^2)/5-7)+1)))*y1*sqrt(y1^2+y3^2)", 
            "y2": "y3", 
            "y3": "-9.8-0.001834*pi*((1-0.0000238*y0)^(2.5))*(1+(1.5/(exp(sqrt(y1^2+y3^2)/5-7)+1)))*y3*sqrt(y1^2+y3^2)"}
quadratic_drag = NODES(state, qd_evolvers, 70)
plt.plot(quadratic_drag.historyx, quadratic_drag.historyy, color="r", label="quadratic drag")
# -----------------------------------------------------------------------------------------------------------------------
state = {'x':0, 'y0': 0, 'y1': 100*sqrt(3)/2, "y2": 0, "y3":50}
ld_evolvers = {'y0': "y1", 
            'y1': "-0.001834*pi*((1-0.0000238*y0)^(2.5))*(1+(1.5/(exp(sqrt(y1^2+y3^2)/5-7)+1)))*y1", 
            "y2": "y3", 
            "y3": "-9.8-0.001834*pi*((1-0.0000238*y0)^(2.5))*(1+(1.5/(exp(sqrt(y1^2+y3^2)/5-7)+1)))*y3"}
linear_drag = NODES(state, ld_evolvers, 90)
plt.plot(linear_drag.historyx, linear_drag.historyy, color="g", label="linear_drag")
# -----------------------------------------------------------------------------------------------------------------------
state = {'x':0, 'y0': 0, 'y1': 100*sqrt(3)/2, "y2": 0, "y3":50}
nd_evolvers = {'y0': "y1", 
            'y1': "0", 
            "y2": "y3", 
            "y3": "-9.8"}
no_drag = NODES(state, nd_evolvers, 80)
plt.plot(no_drag.historyx, no_drag.historyy, color="b", label="no_drag")
# -----------------------------------------------------------------------------------------------------------------------
plt.title("Trajectory of a projectile")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

