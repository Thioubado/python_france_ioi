nombre_copie = int(input())
compteur = 0

for i in range(nombre_copie):
    note = int(input())
    if(note >= 10):
        compteur += 1
print(compteur)