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
    historyy_: list[float]


    def __init__(self, state: dict, evolvers: dict, iterations: int):

        self.dx = 0.01

        self.state = state
        self.evolvers = evolvers

        for yn in self.evolvers:
            self.evolvers[yn] = sympify(self.evolvers[yn])

        '''Run'''
        self.historyx = []
        self.historyy = []
        self.historyy_ = []
        for i in range(0, iterations):
            self.historyx.append(self.state["x"])
            self.historyy.append(self.state["y0"])
            self.historyy_.append(self.state["y2"])
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
state = {'x':0, 'y0': 1, 'y1': 3, "y2": 0, "y3":1}
evolvers = {'y0': "y1", 
            'y1': "cos(y2-y0)*(-y1^2*sin(y2-y0)-9.8*sin(y2))/(2-(cos(y2-y0))^2)", 
            "y2": "y3", 
            "y3": "(-y1^2*tan(y2-y0)-(9.8*sin(y2))/cos(y2-y0))/(0.5*cos(y2-y0)+1/cos(y2-y0))"}

#nodes = NODES(state, evolvers, 500)
#plt.plot(nodes.historyx, nodes.historyy, color="r")
#plt.plot(nodes.historyx, nodes.historyy_, color="b")
# -----------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------
#plt.title("Double Pendulum")
#plt.xlabel("t")
#plt.ylabel("theta_1_d")
#plt.legend()
#plt.show()

