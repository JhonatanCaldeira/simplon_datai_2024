number_list = []
while len(number_list) < 5:
    number = input("Choisissez un nombre positif: ")
    if number.isnumeric():
        if int(number) < 0:
            print("Invalid number!")
        else:
            number_list.append(int(number))

print(number_list)
