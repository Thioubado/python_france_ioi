nombre_de_pommes = int(input())
compteur = 0

for i in range(nombre_de_pommes):
    taille = int(input())
    if(taille >= 150):
        compteur += 1
print(compteur)