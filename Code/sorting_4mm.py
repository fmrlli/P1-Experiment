import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

x_data = []
y_data = []
z_data = []  
value_data = []  
resolution_data = [] 
range_data = []

with open('measurements/data_4.txt', 'r') as file:
    for line in file:
        
        x, y, z, value, resolution, range = line.strip().split(';')
        
        x_data.append(float(x))
        y_data.append(float(y))
        z_data.append(float(z))
        value_data.append(float(value))
        resolution_data.append(float(resolution))  
        range_data.append(float(range))

value_data.sort(reverse = True) #25.75;26.5;0 -> 0.02507
print(value_data)