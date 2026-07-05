# Exercice 2 : Inventaire magasin
nbre_de_rayons = int(input())

nbreDeProduits = int(input())

liste_de_rayons = []

for i in range(nbre_de_rayons):
    liste_des_prix_des_produits = []
    for produit in range(nbreDeProduits):
        prix = float(input())

        # creer uns liste (tableau) des prix pour chaque produit avec les 2 versions possibles
        #liste_des_prix_des_produits += [prix]
        liste_des_prix_des_produits.append(prix)
    
    #Creer une liste avec le prix de chaque produit dans son rayon 
    liste_de_rayons.append(liste_des_prix_des_produits)

print(liste_de_rayons)


