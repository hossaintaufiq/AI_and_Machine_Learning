import numpy as np
import matplotlib.pyplot as plt

# x values
x = np.linspace(0, 5, 100)

# y = e^(-x)
y = np.exp(-x)

# Plot
plt.plot(x, y)

# Labels and title
plt.xlabel("x")
plt.ylabel("e^(-x)")
plt.title("Graph of e^(-x)")

plt.grid(True)

plt.show()