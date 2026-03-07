import matplotlib.pyplot as plt 

# Values of X
x = [0,1,2,3,4]

# probabilities (PMF)
p = [0.08, 0.11, 0.27, 0.33, 0.21]

# compute cdf
cdf = []
cumulative_sum = 0
for prob in p:
    cumulative_sum += prob
    cdf.append(cumulative_sum)

# plotint cdf     
plt.step(x, cdf, where='post', marker='o')

# Labels and title
plt.xlabel("Number of Machines in Use (X)")
plt.ylabel("P(X ≤ x)")
plt.title("Cumulative Distribution Function (CDF)")
plt.grid(True)
plt.show()