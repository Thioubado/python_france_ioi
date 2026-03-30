# Exercice 5 — Compte à rebours
nombre = int(input())

result = nombre
print(result)
for i in range(nombre -1, 0,-1):
    result = result * i
    print(result)