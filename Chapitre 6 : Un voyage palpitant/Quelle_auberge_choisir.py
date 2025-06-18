position_actuelle = int(input())
nbre_de_village_autour_lac = int(input())
compteur = 0
for i in range(nbre_de_village_autour_lac):
    position_chaque_village = int(input())
    if abs(position_chaque_village - position_actuelle) <= 25:
        compteur += 1
print(compteur)