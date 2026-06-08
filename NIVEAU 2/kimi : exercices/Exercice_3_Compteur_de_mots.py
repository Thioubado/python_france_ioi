# Exercice 3 : Compteur de mots 
compteur = [0] * 5

nombre_de_lettres = int(input())

for i in range(nombre_de_lettres):
    lettre = input()

    index = ord(lettre) - ord("A")
    compteur[index] += 1

for compt in compteur:
    print(compt)