import numpy as np
import matplotlib.pyplot as plt

with open('simulation/praktikum001_fort.21 - Copy.txt', 'r') as file:
    data = file.read().split()

values = [float(x) * 1000 for x in data]

space = np.arange(-2.5, 9, 0.0115)

space = space[:1000]

plt.figure(figsize=(12, 6))
plt.plot(space, values)
plt.xlabel('x coordinate [mm]')
plt.ylabel('Energy [GeV]')
plt.grid(True)

plt.show()
