normale = int(input())
nombre = int(input())
compteur = 0

for _ in range(nombre):
    mesures = int(input())
    if abs(mesures - normale) > 5:
        compteur += 1
print(compteur)
