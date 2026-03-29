# Exercice 2 — Puissance

base = int(input())

exposant = int(input())

"""result = pow(base,exposant)
print(result)"""

n = 1
for element in range(exposant):
    n *= base
print(n)