# Exercice C : Enclos pour animaux

nbre_animaux = int(input())

position1_x = int(input())
position1_y = int(input())

min_x = position1_x
max_x = position1_x

min_y = position1_y
max_y = position1_y

for _ in range(nbre_animaux - 1):
    position_x = int(input())
    position_y = int(input())

    if position_x < min_x :
        min_x = position_x

    if position_x > max_x :
        max_x = position_x

    if position_y < min_y :
        min_y = position_y

    if position_y > max_y :
        max_y = position_y

surface =((max_x - min_x) * (max_y - min_y))
print(surface)