nombre_de_tirs = int(input())
compteur = 0
for i in range(nombre_de_tirs):
    x, y = map(int, input().split())
    distance = x * x  + y * y
    if distance <= 100:
        compteur += 1
print(compteur)