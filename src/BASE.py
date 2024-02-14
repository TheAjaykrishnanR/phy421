import re
from sympy import sympify, solve, symbols

class NODES:
    '''
    NODES: Nth Order Differential Equation Solver
    --------------------------------------------------
    Author: Ajaykrishnan R
    --------------------------------------------------
    A dynamic class containing tools to numerically evaluate n-th
    order IVPs
    -------------------------------------------------- 
    '''
    # Static Variables

    '''
    N : Order of the differential equation
    yN = callable function evaluating the N the derivative of y
    method = step function used for the numerical evaluation
    '''

    N: int
    yN: str
    yN_f = None
    method = ["Euler", "RK"]

    # Dynamic Variables

    state: dict = {"x":{"value": None, "evolver": None}, 
                   "y0":{"value": None, "evolver": None}}

    def __init__(self, de: str, init_v: list[str]) -> None:

        # state dict initializer 
        if self.parser(de, init_v):
            print(self.N)
            for i in range(1, self.N + 1):
                self.state[f"y{i}"] = {"value": None, "evolver": None}
        else:
            raise Exception("There was an error parsing the equation entered")
        
        self.add_evolvers_and_init_values_to_state()
        
        print(self.state)
    '''
    Format for entering your differential equation as a string:
    yN = f(x, y0, y1, ..., yN-1) where y{i} denotes the i-th 
    derivative of y with respect to x. 
    '''
    def parser(self, de: str, init_v: list[str]) -> bool:
        if "=" not in de:
            raise Exception("Low IQ Error: Bro you are supposed to input an equation")
        
        LHS, RHS = de.split("=", 1)

        if LHS == "" or RHS == "":
            raise Exception("Low IQ Error: Follow Proper Input Parsing")
        
        LHS_pattern = r"^y\d+"
        RHS_pattern = r"(y\d+|x)"

        if re.match(LHS_pattern, LHS) == None:
            raise Exception("Low IQ Error")
        else:
            self.N = int(LHS[1])
        
        vars_in_RHS = []
        for var in re.findall(RHS_pattern, RHS):
            if var !="x" and int(var[1]) >= self.N:
                raise Exception("Fuckin Prick ! Enter the DE properly")
            vars_in_RHS.append(var)

        _RHS = RHS
        for var in vars_in_RHS:
            _RHS = _RHS.replace(var, "")

        print("leftover ", _RHS, vars_in_RHS)

        residue_pattern = r"[^+-/*]"
        if gib:= re.findall(residue_pattern, _RHS):
            # print(f"re found: {gib}")
            raise Exception(f"Bro just fucking stop it will ya ? What the fuck are these on the RHS: '{_RHS}'")

        try:
            self.yN_f = sympify(RHS)
            self.yN = RHS
        except:
            raise Exception("Fucking prick ! Enter a valid RHS")
        
        return True
    '''
    An N th order IVP gets broken down into N coupled evolvers
    an evolver for a variable y_k is its derivative expressed as functions of the 
    implicit variable x and other STRICTLY FIRST ORDER variables y_i where i runs 
    0 to N without including k ofcourse

    An evolver for a particular variable calculates its value in the next state step
    using the current state as its inputs
    '''
    def add_evolvers_and_init_values_to_state(self):
        
        for idx, var in enumerate(self.state):
            if var == "x":
                self.state["x"]["evolver"] = sympify("dx")

            elif var == f"y{self.N}":
                LHS = symbols(f"y{self.N}")
                RHS = self.yN_f
                self.state[f"y{self.N}"]["evolver"] = solve(LHS - RHS, symbols("x"))[0]

            else:
                self.state[var]["evolver"] = sympify(f"y{int(var[1]) + 1}")
                
        #LHS = symbols("y8")
        #RHS = sympify("y5+y7+y6+x")
        #print(solve(LHS - RHS, symbols("x")))
        #self.state[var]["evolver"] = None
        
    
    def state_shifter(self, state: dict):
        pass
        
nodes = NODES("y8=y5+y7+y6+x", [])