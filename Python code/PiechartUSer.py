import matplotlib.pyplot as plt

n = int(input("Enter number of sections: "))

labels = []
sizes = []

for i in range(n):
    label = input(f"Enter label {i+1}: ")
    value = int(input(f"Enter value for {label}: "))
    labels.append(label)
    sizes.append(value)

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("User Defined Pie Chart")
plt.show()
