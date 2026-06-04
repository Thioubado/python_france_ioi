# Liste de courses
prix = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
total = 0
for i in range(10):
    poids = int(input())
    resultat = prix[i] * poids
    total += resultat
print(total)