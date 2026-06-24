# Exercice 5 : Panier d'achat 
produits = [0] * 50

nombre_de_commandes = int(input())

for i in range(nombre_de_commandes):
    numéro_produit = int(input())
    quantité = int(input())

    numéro_produit -= 1
    produits[numéro_produit] += quantité


for i in range(len(produits)):
    print(f"{i+1} : {produits[i]}")