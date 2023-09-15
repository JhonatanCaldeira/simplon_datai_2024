# 20. Écrivez un programme qui demande à l'utilisateur de
# saisir un mot et affiche si ce
# mot contient plus de 5 caractères en utilisant une boucle "while".

word = ''
while word != 'quit':
    word = input("Choisissez un mot: ")

    if len(word) > 5:
        print(f'Le mot {word} a plus de 5 caractères')
