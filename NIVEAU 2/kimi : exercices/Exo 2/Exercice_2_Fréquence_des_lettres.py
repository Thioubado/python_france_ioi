# Exercice 2 : Fréquence des lettres
compteur = [0] * 26

texte = input("")

for i in texte:

    index = ord(i) - ord("a")
    

    compteur[index] += 1

for i in compteur:
    print(i)