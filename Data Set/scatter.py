import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("pizza_sales_30x30.csv")

plt.scatter(
    df['ingredient_count'],
    df['unit_price'],
    color='green'
)

plt.title('Ingredient Count vs Unit Price')
plt.xlabel('Ingredient Count')
plt.ylabel('Unit Price ($)')
plt.show()