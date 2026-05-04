# Espion étranger
date_de_debut = int(input())
date_de_fin = int(input())

nombre_de_personnes = int(input())

total = 0
for i in range(nombre_de_personnes):
    nombre_d_entrees = int(input())
    if nombre_d_entrees >= date_de_debut and nombre_d_entrees <= date_de_fin :
        total += 1

print(total)