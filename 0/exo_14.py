def upper_case(setence):
    list_of_words = setence.split()
    list_of_words = [word.capitalize() for word in list_of_words]
    return ' '.join(list_of_words)


print(upper_case("J'ai une voiture noire"))
