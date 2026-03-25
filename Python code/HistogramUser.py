import matplotlib.pyplot as plt

# Take input from user
n = int(input("Enter number of values: "))

data = []

for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    data.append(value)

plt.hist(data, bins=5)
plt.title("User Defined Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
