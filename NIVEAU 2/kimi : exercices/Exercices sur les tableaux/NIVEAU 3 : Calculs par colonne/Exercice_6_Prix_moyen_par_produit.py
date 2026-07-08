# Exercice 6 : Prix moyen par produit
nbre_de_rayons = int(input())

nbre_de_produits = int(input())

liste_des_rayons = []

for rayon in range(nbre_de_rayons):
    # Creation du tableau des prix
    liste_des_prix = []
    for produit in range(nbre_de_produits):
        prix = float(input())

        # ajout des prix dans le tableaux de la liste_des_prix cree
        # liste_des_prix += [prix]
        liste_des_prix.append(prix)
    # ajout du tableau des prix dans la liste des rayons
    liste_des_rayons.append(liste_des_prix)

# print liste des rayons
print(liste_des_rayons)

# Creation de la liste des produits
liste_des_produits = []

for produit in range(nbre_de_produits):
    # Initialisation pour pouvoir additionner l'ensemble des prix
    total = 0
    for rayon in range(nbre_de_rayons):
        total += liste_des_rayons[rayon][produit]
    # calcul de la moyenne
    moyenne = total / nbre_de_rayons
    liste_des_produits.append(moyenne)

print(liste_des_produits)

