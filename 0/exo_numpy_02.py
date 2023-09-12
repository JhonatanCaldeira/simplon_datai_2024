# 1. Créez un tableau NumPy contenant 5 valeurs flottantes
# générées aléatoirement entre 0 et 1.

from numpy.random import default_rng

table = default_rng(42).random(5)

print(table)
