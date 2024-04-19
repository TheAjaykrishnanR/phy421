import re
import matplotlib.pyplot as plt

class NODES:

    N: int
    dx: float
    iters: int
    state: dict = {}
    evolvers: dict = {}
    state_history: dict = {}

    def __init__(self, de:str, init: list[str], dx: float, iters: int):

        '''Initialize'''
        self.N, RHS = self.yNparser(de)
        self.dx = dx
        self.iters = iters

        self.state["x"] = None
        self.state_history["x"] = []
        for i in range(0, self.N):
            self.state[f"y{i}"] = None
            self.evolvers[f"y{i}"] = None
            self.state_history[f"y{i}"] = []

        '''Fill in init vars and evolvers'''
        self.initParser(init)
        for yn in self.evolvers:
            if int(yn[1]) == self.N - 1:
                self.evolvers[yn] = RHS
            else:
                self.evolvers[yn] = f"y{int(yn[1]) + 1}"

        '''Run'''
        for i in range(0, 30):
            for yn in self.state_history:
                self.state_history[yn].append(self.state[yn])
            self.rk4()

    def yNparser(self, de: str):
        try:
            LHS, RHS = de.split("=", 1)
        except:
            raise Exception("")
        LHS_pattern = r"y\d+"
        
        if re.match(LHS_pattern, LHS):
            N = int(LHS[1])
        
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

        for idx, Gi in enumerate(Gs):
            
            if idx == 0: 
                Gsw = 0
                _temp = {k:v for k,v in self.state.items() if k != "x"}

            else:
                Gsw = 0.5
                if idx == 3: Gsw = 1
                _temp = {k:v + Gsw*Gs[idx - 1][k]*(self.dx) for k,v in self.state.items() if k != "x"}
            
            _temp["x"] = self.state["x"] + Gsw*self.dx
            
            for yn in _temp:
                exec(f"{yn}={_temp[yn]}")

            for yn in self.state:
                if yn != "x":
                    Gi[yn] = eval(self.evolvers[yn])
                

        '''update the state into the next step'''
        for yn in self.state:
            if yn == "x":
                self.state[yn] += self.dx
            else:
                self.state[yn]+=(self.dx/6)*(Gs[0][yn] + 2*Gs[1][yn] + 2*Gs[2][yn] + Gs[3][yn])
        
        
nodes = NODES("y2=2*y0/x-x*y1", ["x=1", "y0=0", "y1=1"], 0.1, 30)

plt.plot(nodes.state_history["x"], nodes.state_history["y0"])
plt.show()