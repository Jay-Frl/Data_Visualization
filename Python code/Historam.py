import matplotlib.pyplot as plt

# Fixed data
data = [10, 20, 20, 30, 30, 30, 40, 50, 50, 60]

plt.hist(data, bins=5)
plt.title("Normal Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
