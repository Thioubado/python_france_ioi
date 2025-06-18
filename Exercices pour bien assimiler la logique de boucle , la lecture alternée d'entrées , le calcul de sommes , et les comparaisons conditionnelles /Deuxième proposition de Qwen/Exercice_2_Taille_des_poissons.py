nombre_de_poissons_pêchés = int(input())
poisson_inferieur_20_cm = 0
for i in range(nombre_de_poissons_pêchés):
    tailles_en_cm = int(input())
    if tailles_en_cm < 20:
        poisson_inferieur_20_cm += 1
print(poisson_inferieur_20_cm)
