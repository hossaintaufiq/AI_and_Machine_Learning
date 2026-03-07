import matplotlib.pyplot as plt

# Values of X
x = [0, 1, 2, 3, 4]

# Probabilities (PMF)
p = [0.08, 0.11, 0.27, 0.33, 0.21]

# Plot line graph
plt.plot(x, p, marker='o')

# Labels and title
plt.xlabel("Number of Machines in Use (X)")
plt.ylabel("P(X)")
plt.title("Probability Mass Function (PMF)")

# Grid for better view
plt.grid(True)

plt.show()