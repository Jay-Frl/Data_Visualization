# Q1 – Box Plot
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pizza_sales_30x30.csv')
sizes = ['S', 'M', 'L']
data_by_size = [df[df['pizza_size'] == s]['unit_price'].dropna().tolist() for s in sizes]

plt.boxplot(data_by_size, tick_labels=sizes)
plt.xlabel('Pizza Size')
plt.ylabel('Unit Price ($)')
plt.title('Box Plot of Pizza Unit Price by Size')
plt.show()