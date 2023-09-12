
number = -1
while int(number) < 0:
    number = input(
        "Chose one positive number (grater then zero) or zero to exit: ")
    print("")

    if int(number) < 0:
        print("Invalid Number!")
        print("")
    else:
        for i in range(1, int(number)+1):
            print(i)
