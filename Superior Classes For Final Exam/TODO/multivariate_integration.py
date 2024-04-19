from integration import Integrators
from inspect import getfullargspec

def wrapper(f: callable, bounds: list[tuple]):
    vars = getfullargspec(f).args
    if len(bounds) != len(vars):
        raise Exception("variable count does not match the number of bounds")


wrapper(lambda x, y: 0, [(0,1)])

# print(getfullargspec(wrapper))