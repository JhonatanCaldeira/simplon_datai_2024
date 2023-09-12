def check_first_letter(list_string):
    i = 0
    list_of_words = []
    while i < len(list_string):
        if list_string[i][0] in ['a', 'e', 'i', 'o', 'u']:
            list_of_words.append(list_string[i])
        i += 1

    return list_of_words


print(check_first_letter(
    ['banana', 'sucre', 'ecran', 'clavier', 'ordinateur']))
