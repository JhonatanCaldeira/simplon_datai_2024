# 1. Créez une fonction qui prend un tableau NumPy en entrée et renvoie
# un nouveau tableau contenant les éléments triés par ordre croissant.

import numpy as np


def sort_array(table: np):
    table.sort()
    return table


table = np.arange(start=10, stop=0, step=-1)

print(sort_array(table))
