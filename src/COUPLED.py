import re
from sympy import sympify
import matplotlib.pyplot as plt

class NODES:

    N: int # No of variables / no of coupled equations 
    dx: float
    state: dict = {}
    evolvers:dict = {}
    historyx = []
    historyy = []

    def __init__(self, cdes: list[str], N:int,  dx: float, init: list[str]):

        self.dx = dx
        
        self.state = {'x':0, 'y0': 10, 'y1': 1, "y2": 3}
        self.evolvers = {'y0': "10*(y1-y0)", 'y1': "y0*(28-y2)-y1", "y2": "y0*y1-(8/3)*y2"}

        for yn in self.evolvers:
            self.evolvers[yn] = sympify(self.evolvers[yn])

        '''Run'''
        for i in range(0, 50):
            self.historyx.append(self.state["y0"])
            self.historyy.append(self.state["y1"])
            self.rk4()

    def yNparser(self, de: str):
        try:
            LHS, RHS = de.split("=", 1)
        except:
            raise Exception("")
        LHS_pattern = r"y\d+"
        
        if re.match(LHS_pattern, LHS):
            N = int(LHS[1])
        
        try:
            RHS = sympify(RHS)
        except:
            raise Exception("")
        
        return N, RHS
    
    def initParser(self, init: list[str]):
        try:
            for entry in init:
                l, r = entry.split("=", 1)
                self.state[l] = float(r)
        except:
            raise Exception("")


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
        
        
nodes = NODES(["y2=2*y0/x-x*y1"], 3, 0.01, ["x=1", "y0=0", "y1=1"])

plt.plot(nodes.historyx, nodes.historyy)
plt.show()