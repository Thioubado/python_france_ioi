# Exercice 1 — Compter les pairs
nombre = int(input())
resultat = 0

for i in range(nombre):
    chiffre_attribue = int(input())
    if chiffre_attribue % 2 == 0:
        resultat += 1
print(resultat)