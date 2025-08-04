position = int(input())
nombre_d_arrêts_de_bus = int(input())
compteur = 0

for _ in range(nombre_d_arrêts_de_bus):
    position_arret = int(input())
    if abs(position_arret - position) <= 2:
        compteur += 1
print(compteur)