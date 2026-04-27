# https://www.france-ioi.org/algo/task.php?idChapter=647&iOrder=7

nombre_de_maisons = int(input())

abscisse1 = int(input())
ordonnée1 = int(input())

x_min = abscisse1 
x_max = abscisse1 

y_min = ordonnée1
y_max = ordonnée1

for i in range(nombre_de_maisons - 1):
    abscisse = int(input())
    ordonnée = int(input())
    if abscisse < x_min:
        x_min = abscisse

    if abscisse > x_max:
        x_max = abscisse

    if ordonnée < y_min:
        y_min = ordonnée

    if ordonnée > y_max:
        y_max = ordonnée

perimetre = 2 * ((x_max - x_min) + (y_max - y_min))

print(perimetre)