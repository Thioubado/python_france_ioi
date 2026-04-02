# Villes et villages
nombre_de_lieux = int(input())
resultat = 0
for i in range(nombre_de_lieux):
    population_lieux = int(input())
    if population_lieux > 10000:
        resultat += 1
        print(resultat)