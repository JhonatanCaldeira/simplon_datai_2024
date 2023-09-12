# 15. Écrivez une fonction qui prend une chaîne de caractères en entrée
# et renvoie True si cette chaîne est un palindrome
# (c'est-à-dire qu'elle se lit de la même manière de gauche à
# droite et de droite à gauche), sinon renvoie False.

def check_palindrome(word):
    reversed_word = word[::-1]
    return True if word == reversed_word else False


print(check_palindrome('hannah'))
print(check_palindrome('dog'))
