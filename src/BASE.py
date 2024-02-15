import re
from sympy import sympify
import matplotlib.pyplot as plt
class NODES:

    N: int
    dx: float
    state: dict = {}
    evolvers:dict = {}
    historyx = []
    historyy = []

    def __init__(self, de:str, dx: float, init: list[str]):

        '''Initialize'''
        self.N, RHS = self.yNparser(de)
        self.dx = dx
        self.state["x"] = None
        for i in range(0, self.N):
            self.state[f"y{i}"] = None
            self.evolvers[f"y{i}"] = None

        '''Fill in init vars and evolvers'''
        self.initParser(init)
        #self.state = {'x':1, 'y0': 0, 'y1': 1}
        for yn in self.evolvers:
            if int(yn[1]) == self.N - 1:
                self.evolvers[yn] = RHS
            else:
                self.evolvers[yn] = f"y{int(yn[1]) + 1}"
        #self.evolvers = {'y0': "y1", 'y1': "-x*y1+2/x*y0"}

        '''Run'''
        for i in range(0, 30):
            self.historyx.append(self.state["x"])
            self.historyy.append(self.state["y0"])
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

        _temp = {k:v for k,v in self.state.items()}
        G1 = {}
        for yn in self.state:
            if yn != f"y{self.N - 1}" and yn != "x":
                G1[yn] = _temp[f"y{int(yn[1]) + 1}"]
            elif yn != "x":
                G1[yn] = self.evolvers[yn].evalf(subs=_temp)


        _temp = {k:v + G1[k]*(self.dx/2) for k,v in self.state.items() if k != "x"}
        _temp["x"] = self.state["x"] + self.dx/2
        G2 = {}
        for yn in self.state:
            if yn != f"y{self.N - 1}" and yn != "x":
                G2[yn] = _temp[f"y{int(yn[1]) + 1}"]
            elif yn != "x":
                G2[yn] = self.evolvers[yn].evalf(subs=_temp)


        _temp = {k:v + G2[k]*(self.dx/2) for k,v in self.state.items() if k != "x"}
        _temp["x"] = self.state["x"] + self.dx/2
        G3 = {}
        for yn in self.state:
            if yn != f"y{self.N - 1}" and yn != "x":
                G3[yn] = _temp[f"y{int(yn[1]) + 1}"]
            elif yn != "x":
                G3[yn] = self.evolvers[yn].evalf(subs=_temp)
         
        _temp = {k:v + G3[k]*(self.dx/2) for k,v in self.state.items() if k != "x"}
        _temp["x"] = self.state["x"] + self.dx
        G4 = {}
        for yn in self.state:
            if yn != f"y{self.N - 1}" and yn != "x":
                G4[yn] = _temp[f"y{int(yn[1]) + 1}"]
            elif yn != "x":
                G4[yn] = self.evolvers[yn].evalf(subs=_temp)

        for yn in self.state:
            if yn == "x":
                self.state[yn] += self.dx
            else:
                self.state[yn]+=(self.dx/6)*(G1[yn] + 2*G2[yn] + 2*G3[yn] + G4[yn])

nodes = NODES("y2=-x*y1+2/x*y0", 0.1, ["x=1", "y0=0", "y1=1"])

plt.plot(nodes.historyx, nodes.historyy)
plt.show()