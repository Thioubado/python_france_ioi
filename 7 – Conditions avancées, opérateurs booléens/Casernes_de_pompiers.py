# Casernes de pompiers

nombre_de_paires_de_zones = int(input())



for i in range(nombre_de_paires_de_zones):

    abscisse_minimale = int(input())
    abscisse_maximale = int(input())

    ordonnée_minimale = int(input())
    ordonnée_maximale = int(input())

    abscisse_min = int(input())
    abscisse_max = int(input())

    ordonnée_min = int(input())
    ordonnée_max = int(input())

    chevauchement_x = (abscisse_minimale < abscisse_max) and (abscisse_min < abscisse_maximale)
    
    chevauchement_y = (ordonnée_minimale < ordonnée_max) and (ordonnée_min < ordonnée_maximale)

    if chevauchement_x and chevauchement_y:
        print("OUI")
    else:
        print("NON")