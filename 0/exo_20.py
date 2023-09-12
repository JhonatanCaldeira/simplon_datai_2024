# 20. Écrivez un programme qui demande à l'utilisateur de saisir un mot et affiche si ce
# mot contient plus de 5 caractères en utilisant une boucle "while".

word = input("Choisissez un mot: ")
i = 0
while i < len(word):
    i += 1

if i > 5:
    print(f'Le mot {word} a plus de 5 caractères')
