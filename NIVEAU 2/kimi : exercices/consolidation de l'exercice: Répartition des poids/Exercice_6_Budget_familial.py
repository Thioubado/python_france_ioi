# Exercice 6 : Budget familial

# Étape 1 : Lire les données
liste_membres = []

nbre_de_membre = int(input())
nbre_de_categories = int(input())

# Étape 2 : Boucle pour lire

for membre in range(nbre_de_membre):
    depenses_membre = []
    for categorie in range(nbre_de_categories):
        depense = float(input())
        depenses_membre.append(depense)

    liste_membres.append(depenses_membre)

# print(liste_membres)

# Étape 3 : Calculer les moyennes PAR CATÉGORIE

moyennes = []

for categorie in range(nbre_de_categories):
    total = 0
    for membre in range(nbre_de_membre):
        total += liste_membres[membre][categorie]

    moyenne = total / nbre_de_membre
    moyennes.append(moyenne)
# print(moyenne)

# Étape 4 : Afficher les écarts
for membre in range(nbre_de_membre):
    for categorie in range(nbre_de_categories):
        ecart = liste_membres[membre][categorie] - moyennes[categorie]
        print(ecart)