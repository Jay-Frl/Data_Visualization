import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("pizza_sales_30x30.csv")

hourly_orders = df['order_hour'].value_counts().sort_index()

plt.step(
    hourly_orders.index,
    hourly_orders.values,
    color='green',
    where='mid'
)

plt.title('Orders by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Number of Orders')
plt.xticks(hourly_orders.index)
plt.show()