# Comparatif de prix
nbre_de_legumes = int(input())

for i in range(nbre_de_legumes):
    poids = float(input())
    age = float(input())
    prix_de_vente = float(input())

    prix_au_kg = prix_de_vente / poids

    print(prix_au_kg)