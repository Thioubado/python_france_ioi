largeur_du_bas = int(input())
largeur_du_haut = int(input())
total = 0
for element in range(largeur_du_bas, largeur_du_haut - 1, -1):
    total += element * element
print(total)