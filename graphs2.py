from new import fone, euler
import matplotlib.pyplot as plt

m = fone(lambda y, x: -0.5*y**2 + x**2, ["y=10", "x=0"], 10, 0.1, euler)

print(m)
plt.plot([s["x"] for s in m], [s["y"] for s in m])
plt.show()