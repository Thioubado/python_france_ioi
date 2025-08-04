position_actuelle = int(input())
nombre_village = int(input())

meilleur = 100000
for _ in range(nombre_village):
    position_village = int(input())
    distance = abs(position_village - position_actuelle)
    if (distance < meilleur):
        meilleur = distance
print(meilleur)