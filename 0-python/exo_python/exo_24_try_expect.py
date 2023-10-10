try:
    txt = open('Readme.md', 'r')
    print("FILE: ", txt.readline())
    print("")
    txt.write("TEST 02")
except Exception as e:
    print('Erreur: ', e)
finally:
    txt.close()
    print('On a fermé le fichier')
