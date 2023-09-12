# 9. Écrivez une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle liste contenant uniquement les nombres pairs de la liste initiale.

def return_even(number_list: list):
    return [x for x in number_list if x % 2 == 0]


print(return_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
