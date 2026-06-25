# Exercice 6 : Jours de pluie

mois = [0] * 12

nombre_d_observations = int(input())


for i in range(nombre_d_observations):
    numero_du_mois = int(input())
    jours_de_pluie = int(input())

    index = numero_du_mois - 1
    mois[index] += jours_de_pluie

for i in range(len(mois)):
    print(f"{i+1} : {mois[i]}")