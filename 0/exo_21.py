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

    for f in range(1, number):
        print(i)
        i = i_1 + i_2
        i_2 = i_1
        i_1 = i


def fibonnaci_of(n):
    if n in {0, 1}:
        return n

    return fibonnaci_of(n - 1) + fibonnaci_of(n - 2)


fibonnaci(15)
print([fibonnaci_of(n) for n in range(15)])
