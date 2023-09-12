# 21. Écrivez une fonction qui prend un nombre entier en entrée
# et affiche la suite de
# Fibonacci jusqu'à l'ordre de ce nombre. La suite de Fibonacci
# est une séquence d'entiers
# où chaque nombre est la somme des deux nombres précédents. La séquence
# commence généralement par 0 et 1.

def fibonnaci(number):
    i = 0
    i_1 = 1
    i_2 = 0

    while (i < number):
        print(i)
        i = i_1 + i_2
        i_2 = i_1
        i_1 = i


fibonnaci(145)
