# Exercice 3 — Somme des N premiers entiers

chiffre = int(input())

n = 0
for element in range(chiffre+1):
    n += element
print(n)