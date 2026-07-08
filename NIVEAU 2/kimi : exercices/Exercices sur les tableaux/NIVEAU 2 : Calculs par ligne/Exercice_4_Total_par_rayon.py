# Exercice 4 : Total par rayon
nombre_de_rayons = int(input())

nombre_de_produits = int(input())

liste_de_rayons = []

for rayon in range(nombre_de_rayons):
    liste_des_prix = []
    for produit in range(nombre_de_produits):
        prix = float(input())

        #Creation de la liste des produits
        #liste_des_prix += [prix]
        liste_des_prix.append(prix)
    
    # ajout des prix a la liste de rayons pour chaque produit
    liste_de_rayons.append(liste_des_prix)

print(liste_de_rayons)
liste_de_produits = []
for produit in range(nombre_de_produits):
    total = 0
    for rayon in range(nombre_de_rayons):
        total += liste_de_rayons[rayon][produit]
    liste_de_produits.append(total)
print(liste_de_produits)