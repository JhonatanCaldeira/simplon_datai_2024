try:
    num_1 = input('Choisissez le dividende: ')
    num_2 = input('Choisissez le diviseur: ')

    result = int(num_1) / int(num_2)
    print(f"{num_1} / {num_2} = {result}")

except (ZeroDivisionError):
    print('On ne peux pas diviser par zero')
except (Exception) as e:
    print('Erreur: ', e)
else:
    print('Calcule effectue')
finally:
    print('Finally')

print('Après le bloc Try')
