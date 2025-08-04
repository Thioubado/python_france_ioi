position_actuelle = int(input())
nombre_de_village = int(input())

premier_village = int(input())
meilleure_distance = abs(premier_village - position_actuelle)
position_plus_proche = premier_village

for _ in range(nombre_de_village - 1):
    position_de_chaque_village = int(input())
    distanceEntreMaPositionActuelleEtLaPositionDeChaqueVillage = abs(position_de_chaque_village - position_actuelle)
    if distanceEntreMaPositionActuelleEtLaPositionDeChaqueVillage < meilleure_distance:
        meilleure_distance = distanceEntreMaPositionActuelleEtLaPositionDeChaqueVillage
        position_plus_proche = position_de_chaque_village
print(position_plus_proche)