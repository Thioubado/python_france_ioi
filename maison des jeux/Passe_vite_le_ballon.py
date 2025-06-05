position_joueur = int(input())
ecartement_joueur = int(input())
nbre_joueur = int(input())

"""for i in range(position_joueur):
    ecartement_joueur = position_joueur + ecartement_joueur
    print(ecartement_joueur)
"""
for i in range(nbre_joueur):
    position_actuelle = position_joueur + ecartement_joueur * i
    print(position_actuelle)