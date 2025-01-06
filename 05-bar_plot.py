import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [3, 7, 8, 5]

plt.bar(categories, values, color='green')
plt.title("Bar Plot Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
