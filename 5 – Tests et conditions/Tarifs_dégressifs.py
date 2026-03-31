# Tarifs dégressifs
"""heure_D_arrivee = int(input())
prix_chambre = 0

if heure_D_arrivee < 13:
    for i in range(heure_D_arrivee):
        if i == 0:
            prix_chambre += 10
            print(prix_chambre)
        else:
            prix_chambre += 5 
            print(prix_chambre)
        if prix_chambre > 53:
            prix_chambre = 53
            print(prix_chambre)"""

"""heure_arrivee = int(input())
prix_de_depart = 10
resultat = 0

for i in range(heure_arrivee):
    print(i)
    if i == 0:
        print(prix_de_depart)
    else:
        i = prix_de_depart + 5
        print(i)"""
heure = int(input())

prix = 10 + heure * 5
if prix > 53:
    prix = 53
print(prix)      

    

