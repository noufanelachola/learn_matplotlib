import matplotlib.pyplot as plt

fig, ax = plt.subplots()  
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax.plot(x, y, linestyle='--', marker='o')
ax.set_title("Example Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

plt.show()


