def check_first_letter(list_string):
    return [word for word in list_string if word[0] in ['a', 'e', 'i', 'o', 'u']]


print(check_first_letter(
    ['banana', 'sucre', 'ecran', 'clavier', 'ordinateur']))
