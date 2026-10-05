import math
import tkinter as tk

while True:
    try:
        a = float(input("what is your first number: "))
        if a == 0:
            print("a cannot be 0, try again")
        elif a > 1000:
            print("number is too big, trty again")
        else:
            break
    except ValueError:
        print("wrong inout input a valid number ")

while True:
    try:
        b = float(input("what is your second number: "))
        if b == 0:
            print("b cannot be 0, try again")
        elif b > 1000:
            print("number is too big")
        else:
            break
    except ValueError:
        print("wrong input input a valide number")

while True:
    try:
        c = float(input("what is your third number: "))
        if c == 0:
            print("c cannot be 0, tr again")
        elif c > 1000:
            print("number is too big, try again")
        else:
            break
    except ValueError:
        print("wrong input a valid option")

coefficent = (b ** 2) - (4 * a * c)
print("")

if coefficent > 0:
    print("there are two roots")
    x1 = (-b - (coefficent)) / (2 * a)
    x2 = (-b + (coefficent)) / (2 * a)
    print("x1: ", x1)
    print("x2: ", x2)
elif coefficent == 0:
    print("there is one root")
    x = -b / (2 * a)
    print("x: ", x)
else:
    print("there is no root")

def solve():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    coefficent = (b ** 2) - (4 * a * c)
    print("Discreminant:", coefficent)


window = tk.Tk()
window.title("qudratic solution")
window.geometry("400x400")

label_a = tk.Label(window, text="a:")
label_a.pack()

enter_b = tk.Entry(window)
enter_b.pack()

label_b = tk.Label(window, text="b:")
label_b.pack()

enter_a = tk.Entry(window)
enter_a.pack()

label_c = tk.Label(window, text="c:")
label_c.pack()

enter_c = tk.Entry(window)
enter_c.pack()

button = tk.Button(window, text="solve", command=solve)
button.pack()

result = tk.Label(window, text="")
result.pack()




window.mainloop()

