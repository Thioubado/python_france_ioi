# Exercice 8 : Budget familial

"""
Lire un nombre de mois et un nombre de catégories de dépenses.
Pour chaque mois, lire les dépenses par catégorie.
Afficher pour chaque mois : total des dépenses.
Afficher pour chaque catégorie : moyenne mensuelle.
"""


nombre_de_mois = int(input())

nombre_de_categories = int(input())
 
# Creation de la liste des mois
liste_des_mois = []

for mois in range(nombre_de_mois):
    liste_des_depenses = []
    for categorie in range(nombre_de_categories):
        depense = float(input())
        liste_des_depenses.append(depense)
    liste_des_mois.append(liste_des_depenses)

print(liste_des_mois)

liste_des_totaux_par_categorie = []

liste_des_moyennes = []

for categorie in range(nombre_de_categories):
    # initialisation pour pouvoir additionner chaque index
    total = 0
    for mois in range(nombre_de_mois):
        total += liste_des_mois[mois][categorie]
    
    moyenne = total / nombre_de_mois

    liste_des_totaux_par_categorie.append(total)
    liste_des_moyennes.append(moyenne)


# print(liste_des_totaux_par_categorie)
# print(liste_des_moyennes)

print("\nTotaux par catégorie:")
for i in range(len(liste_des_totaux_par_categorie)):
    print(f"Categorie{i+1} : {liste_des_totaux_par_categorie[i]:.2f}")

print("\nMoyennes mensuelles par catégorie :")
for i in range(len(liste_des_moyennes)):
    print(f"Categorie {i + 1} : {liste_des_moyennes[i]:.2f}")

# Étape 4 : Total général
total_general = sum(liste_des_totaux_par_categorie)
print(f"\nTotaux generaux : {total_general:.2f}")

print(f"\nMoyenne mensuelle generale : {total_general / nombre_de_mois:.2f}")