secret_number = 42
number = 0

while number != secret_number:
    number = input("Chosissez un numero: ")
    print(" ")

    if number.isnumeric():
        if int(number) == secret_number:
            print("Felicitations! Vous avez trouvé le nombre secret!")
            break
        elif int(number) < secret_number:
            print(f'Le nombre secret est plus grand que {number}')
            print(" ")
        else:
            print(f'Le nombre secret est plus petit que {number}')
            print(" ")
