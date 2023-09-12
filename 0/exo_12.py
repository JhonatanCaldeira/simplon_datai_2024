# 12. Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie cette chaîne inversée.

def reverse_characters(word):
    word = list(word)
    word.reverse()
    return word


print(reverse_characters('Banana'))
