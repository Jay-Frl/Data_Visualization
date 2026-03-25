import matplotlib.pyplot as plt

# Fixed data
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]

plt.bar(categories, values)
plt.title("Normal Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
