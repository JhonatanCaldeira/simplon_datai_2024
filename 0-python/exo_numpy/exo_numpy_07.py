# 1. Créez une fonction qui prend un tableau NumPy en entrée et renvoie
# la moyenne, la médiane et l'écart type de ses éléments.

import numpy as np


def mean_median_diff(table: np):
    mean = np.mean(table)
    median = np.median(table)
    std = np.std(table)
    print(f'{mean=}, {median=}, {std=}')


table = np.arange(13)

mean_median_diff(table)
