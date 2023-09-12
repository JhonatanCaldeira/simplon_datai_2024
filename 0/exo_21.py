def fibonnaci(number):
    i = 0
    i_1 = 1
    i_2 = 0

    while (i < number):
        print(i)
        i = i_1 + i_2
        i_2 = i_1
        i_1 = i


fibonnaci(145)
