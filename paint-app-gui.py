# Paint App using Tkinter
# Create, doodle, and express yourself!
import tkinter as tk
from tkinter import colorchooser

current_color = "black"

def set_color(new_color):
    global current_color
    current_color = new_color

def paint(event):
    brush_size = size_slider.get()
    x1 = event.x - brush_size // 2
    y1 = event.y - brush_size // 2
    x2 = event.x + brush_size // 2
    y2 = event.y + brush_size // 2
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)

def clear_canvas():
    canvas.delete("all")

def choose_custom_color():
    color = colorchooser.askcolor(title="Pick a Color")[1]
    if color:
        set_color(color)

# Setup window
root = tk.Tk()
root.title("🎨 Prince's Paint App")
root.geometry("850x600")
root.config(bg="#1e1e1e")

# Canvas
canvas = tk.Canvas(root, bg="white", width=820, height=460, bd=3, relief="sunken")
canvas.pack(padx=15, pady=10)
canvas.bind("<B1-Motion>", paint)

# Controls frame
controls = tk.Frame(root, bg="#1e1e1e")
controls.pack(pady=10)

# Preset colors
colors = ["black", "red", "blue", "green", "orange", "purple"]
for col in colors:
    tk.Button(
        controls, bg=col, width=3, height=1,
        command=lambda c=col: set_color(c)
    ).pack(side="left", padx=5)

# Custom color
tk.Button(
    controls, text="🎨 Pick Color", fg="white", bg="#444", command=choose_custom_color
).pack(side="left", padx=10)

# Brush size
tk.Label(controls, text="✏️ Size:", bg="#1e1e1e", fg="white", font=("Segoe UI", 10)).pack(side="left", padx=5)

size_slider = tk.Scale(
    controls, from_=1, to=30, orient="horizontal",
    bg="#1e1e1e", fg="white", troughcolor="#888",
    highlightthickness=0, bd=0
)
size_slider.set(5)
size_slider.pack(side="left", padx=5)

# Clear button
tk.Button(
    controls, text="🧼 Clear", fg="white", bg="#ff4c4c",
    font=("Segoe UI", 10, "bold"), command=clear_canvas
).pack(side="left", padx=20)

root.mainloop()

# 🖌️ Enjoy painting with Prince's Beautiful Paint App! 🎉
