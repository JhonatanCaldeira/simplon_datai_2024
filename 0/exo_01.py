
# 1. Écrivez un programme qui demande à l'utilisateur de saisir un nombre 
# entier positif et affiche tous les nombres de 1 jusqu'à ce nombre (inclus).

number = -1
while int(number) < 0:
    number = input(
        "Chose one positive number (grater then zero) or zero to exit: ")
    print("")

    if number.isnumeric():
        if int(number) < 0:
            print("Invalid Number!")
            print("")
        else:
            for i in range(1, int(number)+1):
                print(i)
    else:
        print(f'{number.upper()} is not a number!')
        print("")
        number = -1
