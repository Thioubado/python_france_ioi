# Étude de marché
nbProduits = int(input())

nbPersonnes = int(input())

compteur = [0] * nbProduits

for i in range(nbPersonnes):
    numéros_des_produits_préférés = int(input())

    #numéros_des_produits_préférés -= 1

    compteur[numéros_des_produits_préférés] += 1
    
for i in range(nbProduits):
    print(compteur[i])