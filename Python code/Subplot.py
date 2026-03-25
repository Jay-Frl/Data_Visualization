import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y_line = [10, 20, 15, 25, 30]
y_scatter = [12, 18, 17, 23, 28]

# Create a figure and one subplot
fig, ax = plt.subplots()

# Line plot
ax.plot(x, y_line, label="Line Plot", color="blue", linewidth=2)

# Scatter plot
ax.scatter(x, y_scatter, label="Scatter Plot", color="red", s=50)

# Labels and title
ax.set_xlabel("X values")
ax.set_ylabel("Y values")
ax.set_title("Line and Scatter on Same Subplot")
ax.legend()

plt.show()
