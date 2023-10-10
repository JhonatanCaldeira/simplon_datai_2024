import numpy as np


def euromillion_01():
    arr_loto = np.arange(1, 51)
    arr_result = []
    rng = np.random.default_rng()

    for n in range(1, 6):
        choice = rng.choice(arr_loto)
        arr_result.append(choice)
        arr_loto = np.delete(arr_loto, np.where(arr_loto == choice))

    print('Solution 1:', arr_result)


def tirage(start, stop, num):
    arr = np.arange(start, stop)
    rng = np.random.default_rng()

    return rng.choice(arr, num, replace=False)


print("Resultat L'euromillion: {0}, {1}*, {2}*".format(
      ', '.join([str(f) for f in tirage(1, 51, 6)]),
      ''.join([str(e1) for e1 in tirage(1, 13, 1)]),
      ''.join([str(e2) for e2 in tirage(1, 13, 1)])
      ))

print('Resultat Loto: {0}, {1}*'.format(
    ', '.join(str(f) for f in tirage(1, 50, 5)),
    ''.join(str(e1) for e1 in tirage(1, 13, 1))
))
# print("L'euromillion :", tirage(1, 51, 6))
# print("L'euromillion :", tirage(1, 13, 1))
# print("L'euromillion :", tirage(1, 13, 1))

# print("Loto: ", tirage(1, 50, 5))
# print("Loto: ", tirage(1, 11, 1))
