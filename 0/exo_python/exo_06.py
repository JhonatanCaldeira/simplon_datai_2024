# 6. Écrivez un programme qui demande à l'utilisateur de saisir 5 nombres
# entiers, acquisition clavier, les stocke dans une liste, puis affiche
# la liste.

number_list = []
while len(number_list) < 5:
    number = input("Choisissez un nombre positif: ")
    if number.isnumeric():
        if int(number) < 0:
            print("Invalid number!")
        else:
            number_list.append(int(number))

print(number_list)
