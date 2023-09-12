# 3. Créez une fonction qui prend un tableau NumPy en entrée
# et renvoie la somme de ses éléments.

import numpy as np


def numpy_table_sum(np_array: np):
    return np_array.sum()


print(numpy_table_sum(np.arange(10)))
