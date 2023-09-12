def check_number(number):
    if number < 0:
        return 'negatif'
    elif number > 0:
        return 'positif'
    else:
        return 'nule'


print(check_number(0))
print(check_number(1))
print(check_number(-1))
