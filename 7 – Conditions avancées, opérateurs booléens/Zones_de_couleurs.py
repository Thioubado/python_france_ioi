# Zones de couleurs
nombre_de_jetons = int(input())

abscisse_feuille = 90
ordonnee_feuille = 70



for i in range(nombre_de_jetons):

    abscisse_jeton = int(input())
    ordonnee_jeton = int(input())

    if not (0 <= abscisse_jeton <= abscisse_feuille and 0 <= ordonnee_jeton <= ordonnee_feuille) :
        print("En dehors de la feuille")
    elif 25 <= abscisse_jeton <= 50 and 20 <= ordonnee_jeton <= 45 :
        print("Dans une zone jaune")
    elif 10 <= abscisse_jeton <= 85 and 10 <= ordonnee_jeton <= 55 :
        print("Dans une zone bleue")
    elif (15 <= abscisse_jeton <= 45 and 60 <= ordonnee_jeton <= 70) or (60 <= abscisse_jeton <= 85 and 60 <= ordonnee_jeton <= 70) :
        print("Dans une zone rouge")
    else:
        print("Dans une zone jaune")