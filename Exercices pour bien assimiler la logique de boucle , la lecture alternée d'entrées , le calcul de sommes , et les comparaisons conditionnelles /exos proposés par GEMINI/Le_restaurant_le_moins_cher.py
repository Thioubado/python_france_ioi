nombre_de_restaurants = int(input())

ligne = input()
valeurs = ligne.split()

nom_restaurant = valeurs[0]
prix_restaurant = int(valeurs[1])

for _ in range(nombre_de_restaurants - 1):
    ligne = input()
    valeurs = ligne.split()
    nom = valeurs[0]
    prix = int(valeurs[1])
    if prix < prix_restaurant:
        prix_restaurant = prix
        nom_restaurant = nom
print(nom_restaurant)

