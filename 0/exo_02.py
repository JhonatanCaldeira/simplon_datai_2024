
def positive_number(list):
    return [x for x in list if x > 0]


list = [-3, 2, 5, 6, 8, -10, -11, -100, 4, 3]

print(positive_number(list))
