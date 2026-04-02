# Exercice 2 — Somme des positifs
nombre = int(input())
resultat = 0

for i in range(nombre):
    chiffre = int(input())
    if chiffre > 0:
        resultat += chiffre

print(resultat)