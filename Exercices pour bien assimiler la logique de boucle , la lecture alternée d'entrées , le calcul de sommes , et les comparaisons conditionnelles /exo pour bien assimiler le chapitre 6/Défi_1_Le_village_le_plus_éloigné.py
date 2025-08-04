position_actuelle = int(input())
nombre_de_village = int(input())

max_distance = 0

for _ in range(nombre_de_village):
    position_village = int(input())
    distance = abs(position_village - position_actuelle)
    if distance > max_distance:
        max_distance = distance
print(max_distance)