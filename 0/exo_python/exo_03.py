# 3. Écrivez une fonction qui prend une liste de mots en entrée et
# renvoie une nouvelle liste contenant les mots dont la première lettre est
# une voyelle (a, e, i, o, u).
def check_first_letter(list_string):
    return [word for word in list_string if word[0] in ['a', 'e', 'i', 'o', 'u']]


print(check_first_letter(
    ['banana', 'sucre', 'ecran', 'clavier', 'ordinateur']))
