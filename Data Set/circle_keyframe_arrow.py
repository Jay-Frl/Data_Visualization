"""
Animated Circle - Basic Version
Arrow keys to move | Tkinter sidebar for Speed, Size, Color, Trail
"""

import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ── State ──────────────────────────────────────────────────────────────────────
state = {
    'x': 0.0, 'y': 0.0,
    'pressed': set(),
    'trail_pts': []
}

COLORS = ['blue', 'red', 'green', 'orange', 'purple', 'cyan']
LIMIT = 0.88

# ── Window ─────────────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Animated Circle - Basic")

# ── Plot ───────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_title("Use Arrow Keys to Move")
ax.grid(True, alpha=0.3)

circle = plt.Circle((0, 0), 0.1, color='blue', zorder=5)
ax.add_patch(circle)
trail_line, = ax.plot([], [], '-', color='blue', alpha=0.4, lw=1.5)
info_text = ax.text(-0.95, -0.95, '', fontsize=8, va='bottom', family='monospace')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=0, rowspan=20)

# ── Sidebar Controls ───────────────────────────────────────────────────────────

# Speed
tk.Label(root, text="Speed", font=('Arial', 10, 'bold')).grid(row=0, column=1, pady=(15, 0))
speed_var = tk.DoubleVar(value=0.04)
tk.Scale(root, from_=0.01, to=0.15, resolution=0.005,
         variable=speed_var, orient='horizontal', length=150).grid(row=1, column=1, padx=15)

# Size
tk.Label(root, text="Size (radius)", font=('Arial', 10, 'bold')).grid(row=2, column=1, pady=(10, 0))
size_var = tk.DoubleVar(value=0.1)
tk.Scale(root, from_=0.02, to=0.35, resolution=0.01,
         variable=size_var, orient='horizontal', length=150).grid(row=3, column=1, padx=15)

# Color
tk.Label(root, text="Color", font=('Arial', 10, 'bold')).grid(row=4, column=1, pady=(10, 0))
color_var = tk.StringVar(value='blue')
color_menu = tk.OptionMenu(root, color_var, *COLORS)
color_menu.config(width=10)
color_menu.grid(row=5, column=1, pady=4)

# Trail toggle
trail_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Show Trail",
               variable=trail_var, font=('Arial', 10)).grid(row=6, column=1, pady=8)

# Reset button
def reset():
    state['x'] = state['y'] = 0.0
    state['trail_pts'].clear()

tk.Button(root, text="Reset Position", command=reset,
          font=('Arial', 10), width=14).grid(row=7, column=1, pady=4)

# Instructions
tk.Label(root, text="\n↑ ↓ ← →  Move\nSliders update live\nTrail shows path",
         font=('Arial', 9), justify='left', fg='gray').grid(row=8, column=1, padx=10, pady=10)

# ── Key Bindings ───────────────────────────────────────────────────────────────
root.bind('<KeyPress>',   lambda e: state['pressed'].add(e.keysym.lower()))
root.bind('<KeyRelease>', lambda e: state['pressed'].discard(e.keysym.lower()))

# ── Animation Loop ─────────────────────────────────────────────────────────────
def update(_frame):
    speed  = speed_var.get()
    radius = size_var.get()
    color  = color_var.get()
    show_trail = trail_var.get()

    lo, hi = -LIMIT, LIMIT

    if 'left'  in state['pressed']: state['x'] = max(lo + radius, state['x'] - speed)
    if 'right' in state['pressed']: state['x'] = min(hi - radius, state['x'] + speed)
    if 'up'    in state['pressed']: state['y'] = min(hi - radius, state['y'] + speed)
    if 'down'  in state['pressed']: state['y'] = max(lo + radius, state['y'] - speed)

    cx, cy = state['x'], state['y']

    circle.center = (cx, cy)
    circle.set_radius(radius)
    circle.set_color(color)
    trail_line.set_color(color)

    if show_trail:
        state['trail_pts'].append((cx, cy))
        if len(state['trail_pts']) > 250:
            state['trail_pts'].pop(0)
        if len(state['trail_pts']) > 1:
            xs, ys = zip(*state['trail_pts'])
            trail_line.set_data(xs, ys)
    else:
        state['trail_pts'].clear()
        trail_line.set_data([], [])

    info_text.set_text(f"X:{cx:+.2f}  Y:{cy:+.2f}  Speed:{speed:.2f}  R:{radius:.2f}")
    canvas.draw_idle()
    return circle, trail_line, info_text

ani = animation.FuncAnimation(fig, update, interval=16, cache_frame_data=False)

root.mainloop()