# Exercice 4 : Températures

sommes = [0] * 7
compteur = [0] * 7

nombre_de_mesures = int(input())

for i in range(nombre_de_mesures):
    numero_piece = int(input())
    temperature = int(input())

    index_piece = numero_piece -1

    sommes[index_piece] += temperature
    compteur[index_piece] += 1

for i in range(7):
    if compteur[i] > 0:
        moyenne = sommes[i] / compteur[i]
    else:
        moyenne = 0

    print(moyenne)
