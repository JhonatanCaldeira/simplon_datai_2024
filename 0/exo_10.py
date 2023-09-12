# 10. Écrivez un programme qui prend une liste de mots en entrée, acquisition clavier, les trie par ordre alphabétique et affiche la liste triée.

words = input("Write some words!")
list_of_word = words.split(" ")
list_of_word.sort()
print(list_of_word)
