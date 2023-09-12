def check_positive(number_list):
    i = 0
    list_of_positive = []
    while i < len(number_list):
        if number_list[i] > 0:
            list_of_positive.append(number_list[i])
        i += 1

    return list_of_positive


list = [-3, 2, 5, 6, 8, -10, -11, -100, 4, 3]

print(check_positive(list))
