# Exercice 1 — Factorielle

"""nombre = int(input())

for i in range(1, nombre + 1):
    print(f"{nombre} = {nombre} * {i}")
print(nombre)"""

nombre = int(input())
resultat = 1
for i in range(1, nombre + 1):
    resultat *= i
print(resultat)