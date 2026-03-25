import matplotlib.pyplot as plt

# Fixed data
labels = ["A", "B", "C", "D"]
sizes = [25, 35, 20, 20]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Normal Pie Chart")
plt.show()
