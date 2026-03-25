import matplotlib.pyplot as plt

n = int(input("Enter number of bars: "))

categories = []
values = []

for i in range(n):
    cat = input(f"Enter category {i+1}: ")
    val = int(input(f"Enter value for {cat}: "))
    categories.append(cat)
    values.append(val)

plt.bar(categories, values)
plt.title("User Defined Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
