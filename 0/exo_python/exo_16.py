# 16. Écrivez un programme qui demande à l'utilisateur de deviner un nombre secret (par exemple 42).
# Le programme indique à l'utilisateur si le nombre à deviner est plus grand ou plus petit que sa proposition
# et continue de demander un nombre tant que l'utilisateur ne trouve pas le nombre secret. Une fois que
# l'utilisateur trouve le nombre secret, affichez un message de félicitations.

import numpy as np

secret_number = np.random.randint(1, 1000)
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
