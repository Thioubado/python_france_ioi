ma_position = int(input())
nombre_de_villes = int(input())

position_premier_ville = int(input())
max_distance = abs(position_premier_ville - ma_position)
ville_plus_eloignee = position_premier_ville

for _ in range(nombre_de_villes - 1):
    position_villes = int(input())
    distance = abs(position_villes - ma_position)
    if distance > max_distance:
        max_distance = distance
        ville_plus_eloignee = position_villes
print(ville_plus_eloignee)

