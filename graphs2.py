from new import fone
import matplotlib.pyplot as plt

m = fone(lambda y: -0.5*y, ["y=10", "x=0"], 10, 0.1)

print(m)
plt.plot([s["x"] for s in m], [s["y"] for s in m])
plt.show()