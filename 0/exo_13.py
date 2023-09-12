# 13. Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie le nombre de mots dans cette chaîne (un mot est séparé par un espace).

def check_number_of_words(setence):
    list_of_words = setence.split()
    return len(list_of_words)


print(check_number_of_words("J'ai une voiture noire"))
