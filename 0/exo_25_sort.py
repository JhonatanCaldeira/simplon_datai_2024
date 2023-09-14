import numpy as np

list = np.random.randint(0, 10, 20)
n = len(list)
print(list)

for i in range(n):
    for j in range(n - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j+1], list[j]

print(list)
