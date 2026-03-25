import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title("Moving Circle")

circle, = ax.plot([], [], 'ro', markersize=10)

def update(frame):
    x = frame
    y = 5
    circle.set_data(x, y)
    return circle,

ani = FuncAnimation(fig, update,
                    frames=np.linspace(0, 10, 100),
                    interval=100)

plt.show()
