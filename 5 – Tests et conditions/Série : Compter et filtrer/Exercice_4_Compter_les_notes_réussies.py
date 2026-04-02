# Exercice 4 — Compter les notes réussies
nombre_d_élèves = int(input())
nbreAyantPlusDe10 = 0
resultat = 0
for _ in range(nombre_d_élèves):
    notes = int(input())
    if notes >= 10:
        nbreAyantPlusDe10 += 1
    resultat += notes
print(f"{nbreAyantPlusDe10} élèves ont réussi")
print(f"Moyenne : {resultat/nombre_d_élèves}")
