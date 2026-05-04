# Maison de l'espion
abscisse_minimale = int(input())
abscisse_maximale = int(input())

ordonnée_minimale = int(input())
ordonnée_maximale = int(input())

nombre_total_de_maisons = int(input())
total = 0
for i in range(nombre_total_de_maisons):
    abscisse = int(input())
    ordonnée = int(input())
    if abscisse >= abscisse_minimale and abscisse <= abscisse_maximale and ordonnée >= ordonnée_minimale and ordonnée <= ordonnée_maximale :
        total += 1

print(total)