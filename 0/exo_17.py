# 17. Écrivez une fonction qui prend un nombre entier en entrée et
# affiche tous les nombres de 1
# jusqu'à ce nombre (inclut) en utilisant une boucle "while".

def final_countdown(number):
    i = 1
    while i <= number:
        print(i)
        i += 1


final_countdown(15)
