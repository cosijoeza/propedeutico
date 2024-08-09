# Calculate mode using statistics.
from statistics import mode

colors = ['red','blue','blue','green','red','red','green']
colors_mode = mode(colors)

print("Mode from ",colors," is ",colors_mode)