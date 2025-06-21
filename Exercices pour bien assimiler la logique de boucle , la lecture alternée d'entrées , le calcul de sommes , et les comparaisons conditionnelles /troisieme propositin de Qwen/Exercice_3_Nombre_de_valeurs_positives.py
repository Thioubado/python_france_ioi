nombre_de_valeurs_à_lire = int(input())
compteur = 0

for i in range(nombre_de_valeurs_à_lire):
    valeur = int(input())
    if valeur > 0:
        compteur += 1
print(compteur)