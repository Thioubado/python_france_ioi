ma_position = int(input())
nombre_de_village = int(input())
#position_plus_eloignee = 0

premier_village = int(input())
meilleure_distance = abs(premier_village - ma_position)
position_plus_eloignee = premier_village

for _ in range(nombre_de_village - 1):
    positionDeChaqueVillage = int(input())
    distanceEntreMaPositionEtLesAutres = abs(positionDeChaqueVillage - ma_position)
    if distanceEntreMaPositionEtLesAutres > meilleure_distance:
        meilleure_distance = distanceEntreMaPositionEtLesAutres
        position_plus_eloignee = positionDeChaqueVillage
print(position_plus_eloignee)