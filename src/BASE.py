from sympy import sympify
import matplotlib.pyplot as plt
class NODES:

    N: int
    x: int
    state: dict = {}
    evolvers:dict = {}
    historyx = []
    historyy = []

    def __init__(self, N: int, x0):
        self.N = N
        
        for i in range(0, self.N):
            self.state[f"y{i}"] = None
            self.evolvers[f"y{i}"] = None
        self.state = {'x':1, 'y0': 0, 'y1': 1}
        self.evolvers = {'y0': "y1", 'y1': "-x*y1+2/x*y0"}

        for i in range(0, 30):
            self.historyx.append(self.state["x"])
            self.historyy.append(self.state["y0"])
            self.rk4()

    def rk4(self):

        _temp = {}

        _temp = {k:v for k,v in self.state.items()}
        G1 = {}
        for yn in self.state:
            if yn != f"y{self.N - 1}" and yn != "x":
                G1[yn] = _temp[f"y{int(yn[1]) + 1}"]
            elif yn != "x":
                G1[yn] = sympify("-x*y1+2/x*y0").evalf(subs=_temp)


        _temp = {k:v + G1[k]*(0.1/2) for k,v in self.state.items() if k != "x"}
        _temp["x"] = self.state["x"] + 0.1/2
        G2 = {}
        for yn in self.state:
            if yn != f"y{self.N - 1}" and yn != "x":
                G2[yn] = _temp[f"y{int(yn[1]) + 1}"]
            elif yn != "x":
                G2[yn] = sympify("-x*y1+2/x*y0").evalf(subs=_temp)


        _temp = {k:v + G2[k]*(0.1/2) for k,v in self.state.items() if k != "x"}
        _temp["x"] = self.state["x"] + 0.1/2
        G3 = {}
        for yn in self.state:
            if yn != f"y{self.N - 1}" and yn != "x":
                G3[yn] = _temp[f"y{int(yn[1]) + 1}"]
            elif yn != "x":
                G3[yn] = sympify("-x*y1+2/x*y0").evalf(subs=_temp)
         
        _temp = {k:v + G3[k]*(0.1/2) for k,v in self.state.items() if k != "x"}
        _temp["x"] = self.state["x"] + 0.1
        G4 = {}
        for yn in self.state:
            if yn != f"y{self.N - 1}" and yn != "x":
                G4[yn] = _temp[f"y{int(yn[1]) + 1}"]
            elif yn != "x":
                G4[yn] = sympify("-x*y1+2/x*y0").evalf(subs=_temp)

        for yn in self.state:
            if yn == "x":
                self.state[yn] += 0.1
            else:
                self.state[yn]+=(0.1/6)*(G1[yn] + 2*G2[yn] + 2*G3[yn] + G4[yn])

nodes = NODES(2, 1)

plt.plot(nodes.historyx, nodes.historyy)
plt.show()