# Exercice 2 — Miroir de code
nombre = int(input())

# boucle pour enregistrer les donnees  remplies
liste_des_points = []
for i in range(nombre):
    point = input()
    #liste_des_points += [point]
    liste_des_points.append(point)
#print(liste_des_points)

liste_inverse = []
for j in range(nombre -1, 0-1, -1):

    if liste_des_points[j] == "N":
        contraire = "S"
    elif liste_des_points[j] == "S":
        contraire = "N"
    elif liste_des_points[j] == "E":
        contraire = "O"
    elif liste_des_points[j] == "O":
        contraire = "E"

    liste_inverse += [contraire]

for i in range(len(liste_inverse)):
    print(liste_inverse[i])
#print(liste_inverse)















"""
Exercice 2 — Miroir de code
Un robot suit un code composé uniquement des lettres N, S, E, O (nord, sud, est, ouest), un caractère par ligne. Affiche le trajet inverse qui le ramène à son point de départ (attention, il faut à la fois inverser l'ordre ET remplacer chaque lettre par son opposé : N↔S, E↔O).

Compétence travaillée : exactement la même logique que ton exercice de la mine, mais avec des lettres au lieu de chiffres — bon exercice de transfert !
"""