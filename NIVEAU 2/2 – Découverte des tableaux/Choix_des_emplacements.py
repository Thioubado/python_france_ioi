# Choix des emplacements
nombre_de_marchands = int(input())

emplacement_du_marchand = [0] * nombre_de_marchands

liste_des_marchands = []
for marchand in range(nombre_de_marchands):
    numero = int(input())

    liste_des_marchands.append(numero)

for i in range(nombre_de_marchands):
    emplacement_du_marchand[liste_des_marchands[i]] = i

for i in emplacement_du_marchand:
    print(i)


""" Cette solution est parfaite mais elle prend beaucoup de ressources et de temps d'execution

nombre_de_marchands = int(input())

liste_des_marchands = []
for marchand in range(nombre_de_marchands):
    numero = int(input())

    liste_des_marchands.append(numero)

for marchand in range(nombre_de_marchands):
    for i in range(nombre_de_marchands):
        if liste_des_marchands[i] == marchand:
            print(i)
"""