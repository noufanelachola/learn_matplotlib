import matplotlib.pyplot as plt

X = [1,2,3,4,5]
Y = [1,2,8,4,5]

plt.plot(X,Y,linestyle='--', marker='o')
plt.title("Basics")
plt.xlabel("X-label")
plt.ylabel("Y-label")

plt.show()