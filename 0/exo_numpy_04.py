# 1. Créez une fonction qui prend deux tableaux NumPy en entrée et
# renvoie le produit scalaire de ces deux tableaux (dot product).

import numpy as np


def produit_scalaire(np_array_01: np, np_array_02: np):
    return np_array_01 @ np_array_02


print(produit_scalaire(np.array([1, 2, 3, 4, 5]), np.array([1, 2, 3, 4, 5])))
