import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots
fig, ax = plt.subplots(2, 2)

# Plot data in each subplot
ax[0, 0].plot([1, 2, 3], [1, 4, 9], label="Quadratic")  # Top-left plot
ax[0, 0].set_title("Top-Left")  # Set title for the subplot
# ax[0, 0].legend()

ax[0, 1].plot([1, 2, 3], [1, 2, 3], label="Linear")  # Top-right plot
ax[0, 1].set_title("Top-Right")
ax[0, 1].legend()

ax[1, 0].plot([1, 2, 3], [3, 2, 1], label="Descending")  # Bottom-left plot
ax[1, 0].set_title("Bottom-Left")
ax[1, 0].legend()

ax[1, 1].plot([1, 2, 3], [9, 4, 1], label="Custom")  # Bottom-right plot
ax[1, 1].set_title("Bottom-Right")
ax[1, 1].legend()

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
