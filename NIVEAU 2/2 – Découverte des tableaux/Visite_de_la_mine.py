# Visite de la mine
nombre_total_de_deplacements = int(input())

tableau_deplacement = []
for i in range(nombre_total_de_deplacements):
    deplacement = int(input())
    tableau_deplacement += [deplacement]
    #tableau_deplacement.append(deplacement)
#print(tableau_deplacement)

tableau_inverse = []
for j in range(nombre_total_de_deplacements -1, 0-1, -1):

    if tableau_deplacement[j] == 1:
        deplacement_oppose = 2
    elif tableau_deplacement[j] == 2:
        deplacement_oppose = 1
    elif tableau_deplacement[j] == 3:
        deplacement_oppose = 3
    elif tableau_deplacement[j] == 4:
        deplacement_oppose = 5
    elif tableau_deplacement[j] == 5:
        deplacement_oppose = 4
    
    tableau_inverse += [deplacement_oppose]

for i in range(len(tableau_inverse)):
    print(tableau_inverse[i])
#print(tableau_inverse)