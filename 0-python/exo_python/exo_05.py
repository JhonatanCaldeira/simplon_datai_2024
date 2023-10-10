# 5. Écrivez un programme qui demande à l'utilisateur de saisir un mot et
# affiche si ce mot contient plus de 5 caractères.

word = input("Write a word: ")
if len(word) > 5:
    print(f'The word {word} has more than 5 characters')
