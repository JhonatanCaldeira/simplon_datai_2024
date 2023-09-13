# 1. Créez une fonction qui prend un tableau NumPy en entrée et renvoie
# un nouveau tableau où tous les éléments inférieurs à 5 sont remplacés
# par 0 et tous les éléments supérieurs ou égaux à 5 sont remplacés par 1.

import numpy as np


def replace_by_0_1(table: np):
    table[table < 5] = 0
    table[table >= 5] = 1
    print(table)


def replace_by_0_1_v2(table: np):
    np.place(table, table < 5, [0])
    np.place(table, table >= 5, [1])
    print(table)


table = np.arange(11)
replace_by_0_1(table)

table = np.arange(11)
replace_by_0_1_v2(table)
