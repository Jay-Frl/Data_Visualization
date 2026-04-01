# Q2 – Scatter Plot with outlier, clusters, positive correlation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('pizza_sales_30x30.csv')
x = df['unit_price'].values
y = df['total_price'].values

plt.scatter(x, y, label='Orders', alpha=0.7)

# Add outlier (quantity=2 at low price)
plt.scatter([10.5], [22.0], color='red', s=120, zorder=5, label='Outlier')

# Trend line
m, b = np.polyfit(x, y, 1)
xline = np.linspace(x.min(), x.max(), 100)
plt.plot(xline, m*xline + b, 'k--', label='Positive Correlation')

plt.xlabel('Unit Price ($)')
plt.ylabel('Total Price ($)')
plt.title('Scatter Plot: Unit Price vs Total Price')
plt.legend()
plt.show()