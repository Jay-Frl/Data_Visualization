import matplotlib.pyplot as plt

# Take input from user
n = int(input("Enter number of points: "))

x = []
y = []

for i in range(n):
    x_value = int(input(f"Enter x value {i+1}: "))
    y_value = int(input(f"Enter y value {i+1}: "))
    x.append(x_value)
    y.append(y_value)

plt.plot(x, y)
plt.title("User Defined Line Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
