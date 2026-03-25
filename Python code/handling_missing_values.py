import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create simple dataset with missing values
data = {
    "Marks": [80, 90, np.nan, 70, np.nan, 85]
}

df = pd.DataFrame(data)

print("Before Handling Missing Values:")
print(df)

# Visualize missing values (Before)
plt.figure(figsize=(5,3))
plt.title("Before Handling Missing Values")
plt.imshow(df.isnull(), cmap="gray", aspect="auto")
plt.yticks(range(len(df)))
plt.xticks([0])
plt.show()

# Fill missing values with mean
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

print("\nAfter Handling Missing Values:")
print(df)

# Visualize missing values (After)
plt.figure(figsize=(5,3))
plt.title("After Handling Missing Values")
plt.imshow(df.isnull(), cmap="gray", aspect="auto")
plt.yticks(range(len(df)))
plt.xticks([0])
plt.show()
