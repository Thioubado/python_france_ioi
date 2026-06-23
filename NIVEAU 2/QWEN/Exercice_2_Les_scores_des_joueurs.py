# Exercice 2 : Les scores des joueurs
joueurs = [0, 0, 0, 0, 0]

nbre_opérations = int(input())

for i in range(nbre_opérations):
    numéro_du_joueur = int(input())
    points_gagnés = int(input())

    numéro_du_joueur -= 1
    joueurs[numéro_du_joueur] += points_gagnés

for i in joueurs:
    print(i) 