# 1. Créez une fonction qui prend un tableau NumPy en entrée et renvoie un
# nouveau tableau contenant uniquement les éléments uniques du tableau d'origine.

import numpy as np


def get_unique(table: np):
    return np.unique(table)


def get_unique_v2(table: np):
    return np.asarray([f for f in table if len(table[table == f]) == 1])


table = np.array([1, 1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 8, 8, 9])
print(get_unique(table))

table = np.array([1, 1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 8, 8, 9])
print(get_unique_v2(table))
