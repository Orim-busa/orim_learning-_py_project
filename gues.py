import random

while True:
    num = random.randint(1, 100)
    try:
        guess = float(input("what is your number: "))
        if guess == "Exit":
            print("thanks for playing with us.")
            break
    except ValueError:
        print("wrong input. input the correct number.")
        break
    print(num)

    if guess < 1:
        print("Below range. try again")
    elif guess > 100:
        print("Above range. try again")
    elif guess > num:
        print("Too big. try again")
    elif guess < num:
        print("Too small. Try again")
    else:
        print("correct")
        break
