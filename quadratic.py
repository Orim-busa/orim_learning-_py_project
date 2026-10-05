import math
try:
    a = float(input("what your first number: "))
    b = float(input("what your second number: "))
    c = float(input("what your third number: "))
    coeficent = (b ** 2) - (4 * a * c)
    print("Descreminant:", coeficent)
    if coeficent > 0:
        print("there are two real roots")
        x1 = (-b + math.sqrt(coeficent)) / (2 * a)
        x2 = (-b - math.sqrt(coeficent)) / (2 * a)
        print("x1:", x1)
        print("x2:", x2)
    elif coeficent == 0:
        print("there is one real root")
        x1 = -b / (2 * a)
        print("x1:", x1)
except:
    print("wrong inout input a valid number")
