# Exercice 6

tableau = [0] * 10

nbOperations = int(input())

for i in range(nbOperations):
    numero = int(input())
    quantite = int(input())

    numero = numero - 1
    tableau[numero] = tableau[numero] + quantite
print(tableau)