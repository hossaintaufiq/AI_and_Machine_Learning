import numpy as np
import matplotlib.pyplot as plt

# x values
x = np.linspace(0, 4, 100)

# pdf function
f = x / 8

plt.plot(x, f)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Probability Density Function f(x) = x/8")
plt.show()