import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('measurements/data_4.txt', sep=';', header=None)

data = np.array(data)

# Extract x, y, z, and Dose
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]
dose = data[:, 3]

# Calculate radius
radius = np.sqrt(x**2 + y**2 + z**2)

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(radius, dose, alpha=0.5)
plt.xlabel('Radius')
plt.ylabel('Dose')
plt.title('Dose vs Radius')
plt.grid(True)
plt.show()