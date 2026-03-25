import matplotlib.pyplot as plt

# Fixed data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.step(x, y)
plt.title("Stair Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
