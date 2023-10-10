# 8. Écrivez une fonction qui prend une liste de mots en entrée et renvoie
# une nouvelle liste contenant la longueur de chaque mot.

def word_length(word_list: list):
    return [len(word) for word in word_list]


print(word_length(['banana', 'sucre', 'ecran', 'clavier', 'ordinateur']))
