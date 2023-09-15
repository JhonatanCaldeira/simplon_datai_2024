# 2. Écrivez une fonction qui prend une liste de nombres en entrée et renvoie
# une nouvelle liste contenant uniquement les nombres positifs.

def positive_number(list_of_number):
    return [x for x in list_of_number if x > 0]


list = [-3, 2, 5, 6, 8, -10, -11, -100, 4, 3]

print(positive_number(list))
