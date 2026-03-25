import pandas as pd
import matplotlib.pyplot as plt

# Load pizza sales dataset
df = pd.read_csv("pizza_sales_30x30.csv")

df_sorted = df.sort_values('unit_price')

fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    df_sorted['unit_price'],
    df_sorted['total_price'],
    marker='o',
    color='#e63946',
    linewidth=2,
    markersize=6,
    markerfacecolor='white',
    markeredgecolor='#e63946',
    markeredgewidth=1.5
)

ax.set_title('Unit Price vs Total Price', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Unit Price ($)', fontsize=11)
ax.set_ylabel('Total Price ($)', fontsize=11)
ax.spines[['top', 'right']].set_visible(False)
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.xaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig("unit_vs_total_price.png", dpi=150, bbox_inches='tight')
plt.show()