import re
from collections.abc import Callable
from inspect import getfullargspec

# arg_vp -> arg value pairs

def fone(y_p: callable, init: list[str], x_f: int, dx: float, 
         next_step: Callable[[], dict], *args_for_next_step) -> list:
    
    y_p_args: list[str] = getfullargspec(y_p).args
    y_p_args_order: int= []
    intermediate_state_dict: dict = {"x": None, "y": None}
    state_history_list: list[dict] = []

    # To find the order of the DE
    arg_pattern: str= r"^y\d+$"
    
    for idx, arg in enumerate(y_p_args):
        if arg == "y":
            y_p_args_order.append(0)
        elif arg.startswith("y") and arg.removeprefix("y") != "":
            y_p_args_order.append(int(arg.removeprefix("y")))
            if not re.match(arg_pattern, arg) and arg != "x":
                raise Exception("Bad y_p formatting: y[0-9] !")
            
        elif arg == "x" and idx != len(y_p_args) - 1:
            raise Exception("Bad y_p formatting: x_pos !")
        
    order: int = max(y_p_args_order)

    # Filling the master update dict
    for i in range(1, order + 2):
        intermediate_state_dict[f"y{i}"] = None

    for _init in init:
        try:
            _key_pairs = _init.split("=", 1)
            intermediate_state_dict[_key_pairs[0]] = int(_key_pairs[1])
        except:
            raise Exception("Follow init string formatting !")
    
    print(y_p_args)
    print(y_p_args_order)    
    print(order)
    print([i for i in range(1, order + 2)])
    print(intermediate_state_dict)
        
    # check init arg sufficiency
    for arg in intermediate_state_dict:
        if arg != "y1" and intermediate_state_dict[arg] == None:
            raise Exception("Insufficient init conditions")
        
    # build yp arg list for calling it
    arg_value_chain = []
    for arg in y_p_args:
        arg_value_chain.append(intermediate_state_dict[arg])

    intermediate_state_dict["y1"] = y_p(*arg_value_chain)

    while intermediate_state_dict["x"] <= x_f:

        state_history_list.append(intermediate_state_dict.copy())

        intermediate_state_dict = next_step(intermediate_state_dict, order, dx, *args_for_next_step)
        
        intermediate_state_dict["x"] += dx

        arg_value_chain.clear()
        for arg in y_p_args:
            arg_value_chain.append(intermediate_state_dict[arg])

        intermediate_state_dict[f"y{order + 1}"] = y_p(*arg_value_chain)

    return state_history_list

def euler(intermediate_state_dict: dict, order:int, dx: float) -> dict:

    for i in range(0, order + 1):
            if i == 0:
                intermediate_state_dict["y"] += intermediate_state_dict[f"y{i + 1}"]*dx
            else:
                intermediate_state_dict[f"y{i}"] += intermediate_state_dict[f"y{i + 1}"]*dx  
    
    return intermediate_state_dict

def rk_2(intermediate_state_dict: dict, order:int, dx: float, params: list[float],
         y_p: callable) -> dict:

    al, bt, a, b = params

    for i in range(0, order + 1):

        if i == 0:
            k1 = intermediate_state_dict["y"]
            k2 = y_p(intermediate_state_dict["y"] + bt*dx*k1, _x +  al*dx)
            intermediate_state_dict["y"] += (a*k1 + b*k2)*dx
        else:
            intermediate_state_dict[f"y{i}"] += (a*k1 + b*k2)*dx  

    

    return intermediate_state_dict

# fone(lambda y: -0.5*y, ["y=10", "x=0"], 10, 0.1, euler)