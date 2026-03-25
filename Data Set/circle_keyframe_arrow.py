import tkinter as tk

# Keyframes: (x, y) — fixed size
keyframes = [
    (150, 200),
    (350, 100),
    (550, 200),
    (400, 320),
    (200, 320),
]

RADIUS = 40
current = 0
step = 0
STEPS = 30
animating = False
start = keyframes[0]
end = keyframes[0]

def lerp(a, b, t):
    return a + (b - a) * t

def draw(x, y):
    canvas.delete("all")
    canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS,
                       fill="royalblue", outline="")
    label.config(text=f"Keyframe {current + 1} / {len(keyframes)}")

def animate():
    global step, animating
    t = step / STEPS
    x = lerp(start[0], end[0], t)
    y = lerp(start[1], end[1], t)
    draw(int(x), int(y))
    step += 1
    if step <= STEPS:
        root.after(16, animate)
    else:
        animating = False

def go(direction):
    global current, step, animating, start, end
    if animating:
        return
    next_kf = current + direction
    if 0 <= next_kf < len(keyframes):
        start = keyframes[current]
        end = keyframes[next_kf]
        current = next_kf
        step = 0
        animating = True
        animate()

root = tk.Tk()
root.title("Circle Animation")

canvas = tk.Canvas(root, width=700, height=400, bg="#f0f0f0")
canvas.pack()

label = tk.Label(root, text="Keyframe 1 / 5", font=("Arial", 12), pady=5)
label.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="◀ Prev", command=lambda: go(-1), font=("Arial", 13), padx=16, pady=6).pack(side="left", padx=10)
tk.Button(btn_frame, text="Next ▶", command=lambda: go(+1), font=("Arial", 13), padx=16, pady=6).pack(side="left", padx=10)

root.bind("<Left>",  lambda e: go(-1))
root.bind("<Right>", lambda e: go(+1))

draw(*keyframes[0])
root.mainloop()