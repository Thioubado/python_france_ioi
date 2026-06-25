# Répartition du poids

nbCharrettes = int(input())

total = 0
poids_charrettes = []

for i in range(nbCharrettes):
    poids = float(input())

    # stocker les poids
    poids_charrettes.append(poids)

    # calculer le poids total
    total += poids

moyenne = total / nbCharrettes

for i in range(nbCharrettes):
    print(moyenne - poids_charrettes[i])