nombre_d_écrevisses_pêchées_par_les_jeunes = int(input())
compteur = 0
for i in range(nombre_d_écrevisses_pêchées_par_les_jeunes):
    taille_de_chaque_écrevisse = int(input())
    if taille_de_chaque_écrevisse >= 12:
        compteur += 1
print(compteur)