from sympy import *
from DoublePendulum import NODES

state1 = {'x':0, 'y0': 0.01, 'y1': 0, "y2": 0.01, "y3":0}
state2 = {'x':0, 'y0': 0.0101, 'y1': 0, "y2": 0.0102, "y3":0}
evolvers = {'y0': "y1", 
            'y1': "(-9.8*3*sin(y0)-9.8*sin(y0-2*y2)-2*sin(y0-y2)*((y3^2)+(y1^2)*cos(y0-y2)))/(3-cos(2*y0-2*y2))", 
            "y2": "y3", 
            "y3": "2*sin(y0-y2)*((y1^2)*2+9.8*2*cos(y0)+(y3^2)*cos(y0-y2))/(3-cos(2*y0-2*y2))"
            }




'''
state1 = {'x':0, 'y0': 0.1, 'y1': 0}
evolvers = {'y0': "y1", 
            'y1': "-9.8*sin(y0)"
            }

'''
dp1 = NODES(state1, evolvers, 5000)
dp2 = NODES(state2, evolvers, 5000)

'''
with open("theta", "w") as file:
    for item in dp1.historyy:
        file.write(str(item) + "\n")

'''



with open("theta1_1values", "w") as file:
    for item in dp1.historyy:
        file.write(str(item) + "\n")
        
with open("theta2_1values", "w") as file:
    for item in dp1.historyy_:
        file.write(str(item) + "\n")

with open("theta1_2values", "w") as file:
    for item in dp2.historyy_:
        file.write(str(item) + "\n")

with open("theta2_2values", "w") as file:
    for item in dp2.historyy_:
        file.write(str(item) + "\n")

