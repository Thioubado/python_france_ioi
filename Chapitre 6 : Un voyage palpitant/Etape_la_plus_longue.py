nombre_de_jours = int(input())
compteur = 0
for i in range(nombre_de_jours):
    chaque_jour = int(input())
    if chaque_jour > compteur:
        compteur = chaque_jour
print(compteur)