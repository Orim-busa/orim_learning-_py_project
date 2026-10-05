while True:
    choice = input("do you want to  convert 0.exit_program  1.celcius to fahrenheit or 2.fahrenheit to celsius?: ")
    if choice == "0":
        print("exiting the program")
        break
    elif choice == "1":
        print("You have chosen to convert celcius to fahrenheit")
        celcius = float(input("what is your temperature in celsius: "))
        fahrenheit = (celcius * 9/5) + 32
        print("Temperature in celsius: ", celcius)
    
    elif choice == "2":
        print("You have chosen to convert fahrenheit to celcius")
        fahrenheit = float(input("what is your temperature in fahrenheit: "))
        celcius = (fahrenheit - 32) * 5/9
        print("Temperature in Fahrenheit: ",fahrenheit)
    else:
        print("Invalid choice. pick a valid option")


    if celcius > 30:
        print("It is hot")
    elif celcius == 30:
        print("Temperature is exaclly 30")
    else:
        print("Not hot")







