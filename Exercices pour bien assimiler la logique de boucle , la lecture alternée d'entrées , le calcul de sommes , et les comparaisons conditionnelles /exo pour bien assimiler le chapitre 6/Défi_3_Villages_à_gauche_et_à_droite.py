ma_position = int(input())
nombre_de_village = int(input())

gauche = 0
droite = 0

for _ in range(nombre_de_village):
    position = int(input())
    if position < ma_position:
        gauche += 1
    else:
        droite += 1
print(gauche, droite)


