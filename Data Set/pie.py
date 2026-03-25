import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("pizza_sales_30x30.csv")

category_counts = df['pizza_category'].value_counts()

category_counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Pizza Category Distribution')
plt.ylabel('')
plt.show()