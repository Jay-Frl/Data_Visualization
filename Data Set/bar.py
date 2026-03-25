import pandas as pd
import matplotlib.pyplot as plt

# Load pizza sales dataset
df = pd.read_csv("pizza_sales_30x30.csv")

category_counts = df['pizza_category'].value_counts()

fig, ax = plt.subplots(figsize=(7, 5))

bars = ax.bar(
    category_counts.index,
    category_counts.values,
    color=['#e63946', '#f4a261', '#2a9d8f', '#457b9d'],
    edgecolor='white',
    linewidth=0.8,
    width=0.5
)

# Add value labels on top of each bar
for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.1,
        str(int(bar.get_height())),
        ha='center', va='bottom',
        fontsize=11, fontweight='bold', color='#333333'
    )

ax.set_title('Pizza Category Distribution', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Category', fontsize=11)
ax.set_ylabel('Count', fontsize=11)
ax.spines[['top', 'right']].set_visible(False)
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig("pizza_category_distribution.png", dpi=150, bbox_inches='tight')
plt.show()