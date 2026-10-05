import math
import tkinter as tk

def solve():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        result.config(text="Invalid input, enter valid numbers")
        return
    if a == 0:
        result.config(text="a cannot be 0")
        return
    coefficient = (b ** 2) - (4 * a * c)
    if coefficient > 0:
        x1 = (-b + math.sqrt(coefficient)) / (2 * a)
        x2 = (-b - math.sqrt(coefficient)) / (2 * a)
        result.config(text=f"Discriminant: {coefficient}\nTwo roots\nx1: {x1}\nx2: {x2}")
    elif coefficient == 0:
        x1 = -b / (2 * a)
        result.config(text=f"Discriminant: {coefficient}\nOne root\nx1: {x1}")
    else:
        result.config(text=f"Discriminant: {coefficient}\nNo real roots")

window = tk.Tk()
window.title("Quadratic Solver")

tk.Label(window, text="a:").grid(row=0, column=0)
entry_a = tk.Entry(window)
entry_a.grid(row=0, column=1)

tk.Label(window, text="b:").grid(row=1, column=0)
entry_b = tk.Entry(window)
entry_b.grid(row=1, column=1)

tk.Label(window, text="c:").grid(row=2, column=0)
entry_c = tk.Entry(window)
entry_c.grid(row=2, column=1)

tk.Button(window, text="Solve", command=solve).grid(row=3, column=0, columnspan=2)

result = tk.Label(window, text="")
result.grid(row=4, column=0, columnspan=2)

window.mainloop()