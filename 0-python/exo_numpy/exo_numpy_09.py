# 1. Créez un tableau NumPy 2D de taille 3x3 contenant des valeurs
# entières générées aléatoirement entre 1 et 10.

import numpy as np

table = np.random.randint(10, size=(3, 3))
print(table)
