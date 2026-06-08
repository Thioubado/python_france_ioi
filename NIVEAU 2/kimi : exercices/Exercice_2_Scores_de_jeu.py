# Exercice 2 : Scores de jeu
liste_joueur = [0] * 10

nombre_de_tours = int(input())

for i in range(nombre_de_tours):
    numero_joueur = int(input())
    points = int(input())

    #
    index = numero_joueur - 1
    liste_joueur[index] += points

for i in liste_joueur:
    print(i)
