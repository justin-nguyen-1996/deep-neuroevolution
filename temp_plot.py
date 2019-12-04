# temp_plot.py

import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(1,1,1)

x = [0, 10, 20, 30, 40, 50]
y = [121, 156, 164, 225, 1271, 232]
ax.plot(x, y, label='NSR, BC = RAM')

x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = [40, 154, 209, 364, 1127, 2445, 2781, 2921, 2865, 2763, 2813]
ax.plot(x, y, label='NSR, BC = Ice blocks stepped on')

x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = [0, 0, 0, 0, 70, 0, 60, 80, 0, 0, 0]
ax.plot(x, y, label='NS, BC = Ice blocks stepped on')

x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = [52, 174, 253, 321, 1006, 1543, 1890, 2213, 2872, 2813, 2792]
ax.plot(x, y, label='ES')

plt.title('Frostbite BC comparisons')
plt.xlabel('Number of iterations')
plt.ylabel('Reward score')
# Shrink the plot's width to 80%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])
# Place center left of legend at x/y coordinate (1, 0.5)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
