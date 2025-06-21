nombre_de_jours = int(input())
compteur = 0

for i in range(nombre_de_jours):
    pas_par_jour = int(input())
    if pas_par_jour > compteur:
        compteur = pas_par_jour
if compteur > 0:
    print(compteur)
else:
    print("Aucun pas")