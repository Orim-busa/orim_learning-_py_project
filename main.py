from tool import calculator
while True:

    print("==========CALCULATOR==========")
    print("1. add")
    print("2. subtract")
    print("3. devide")
    print("4. multiply")
    print("5. EXIT")

    choice = input("select an option: ")
    if choice == "5":
        print("goodbye ")
        break
    try:
        num1 = float(input("what is your number: "))
        num2 = float(input("what is your number: "))
    except ValueError:
        print("enter a valid number")
    if choice == "1":
        print("result:", calculator.add(num1, num2))
    elif choice == "2":
        print("result:", calculator.subtract(num1, num2))
    elif choice == "3":
        print("result:", calculator.devide(num1, num2))
    elif choice == "4":
        print("result:", calculator.multiply(num1, num2))
    else:
        print("invalid option")

