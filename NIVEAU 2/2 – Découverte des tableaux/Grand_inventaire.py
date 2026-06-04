# Grand inventaire

tableau = [0] * 10

nbOperations = int(input())

for i in range(nbOperations):
    numero_ingredient = int(input())
    quantite = int(input())
    tableau[numero_ingredient - 1] += quantite

for i in tableau:
    print(i)