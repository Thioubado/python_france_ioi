# Exercice 3 — Le plus grand
nombre = int(input())
maximum = int(input())

for _ in range(nombre -1):
    chiffre = int(input())
    if chiffre > maximum:
        maximum = chiffre
print(maximum)