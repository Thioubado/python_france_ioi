# Exercice 10 : Stock magasin
nombre_de_rayons = int(input())

nombre_de_produits = int(input())

# Étape 1 : Lecture des données
tableau_des_rayons = []
#tableau_des_produits = []


for rayon in range(nombre_de_rayons):
    ligne_rayon = []
    for produit in range(nombre_de_produits):
        prix = float(input())
        quantite = int(input())

        valeur = quantite * prix

        ligne_rayon.append(valeur)

    tableau_des_rayons.append(ligne_rayon)

print("Tableau des valeurs :", tableau_des_rayons)


# ============================================
# Étape 2 : Valeur totale par rayon
# ============================================
print("\nValeurs totales par rayon :")

# nouvelle liste
valeurs_totales_rayons = [] 
for rayon in range(nombre_de_rayons):
    total_rayon = 0
    for produit in range(nombre_de_produits):
        total_rayon += tableau_des_rayons[rayon][produit]
    # le for ci-dessus peut etre remplace par : total = sum(nombre_de_rayons[rayon])
    #total = sum(nombre_de_rayons[rayon])

    valeurs_totales_rayons.append(total_rayon)
    print(f"Rayon {rayon + 1} : {total_rayon:.2f}")


plus_cher_rayon = max(valeurs_totales_rayons)
index_plus_cher = valeurs_totales_rayons.index(plus_cher_rayon)

print(f"\nRayon le plus cher : Rayon {index_plus_cher + 1} ({plus_cher_rayon:.2f})")

# ============================================
# Étape 4 : Produit le plus cher du magasin
# ============================================
for rayon in range(nombre_de_rayons):
    toutes_les_valeurs = []
    for produit in range(nombre_de_produits):
        toutes_les_valeurs.append(tableau_des_rayons[rayon][produit])

plus_cher_produit = max(toutes_les_valeurs)


print(f"Produit le plus cher: {plus_cher_produit:.2f} ")

# ============================================
# Étape 5 : Meilleur produit par rayon (optionnel)
# ============================================
print("\nMeilleur produit par rayon :")
for rayon in range(nombre_de_rayons):
    meilleur = max(tableau_des_rayons[rayon])
    index_produit = tableau_des_rayons[rayon].index(meilleur) 
    print(f"  Rayon {rayon + 1} : Produit {index_produit + 1} ({meilleur:.2f})")
    #print(f"  Rayon {rayon + 1} : Produit {index_produit + 1} ({meilleur:.2f})")




"""
Lire un nombre de rayons et un nombre de produits.
Pour chaque produit, lire : prix et quantité en stock.
Calculer :
- Valeur totale du stock par rayon
- Produit le plus cher du magasin
- Rayon avec la plus grande valeur totale
"""