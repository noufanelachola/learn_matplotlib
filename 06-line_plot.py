import matplotlib.pyplot as plt

# Data
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Line plot
plt.plot(x, y, label="y = x^2")  # Plot with a label
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()  # Show legend
plt.grid(True)  # Add grid lines
plt.show()
