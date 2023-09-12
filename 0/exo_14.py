# 14. Écrivez une fonction qui prend une chaîne de caractères
# en entrée et renvoie une nouvelle chaîne où chaque mot est en majuscules.

def upper_case(setence):
    list_of_words = setence.split()
    list_of_words = [word.capitalize() for word in list_of_words]
    return ' '.join(list_of_words)


print(upper_case("J'ai une voiture noire"))
