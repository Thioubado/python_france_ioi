# Bornes kilométriques
Borne_depart = int(input())
Borne_arrivee = int(input())

if Borne_depart > Borne_arrivee:
    distance = Borne_depart - Borne_arrivee
    print(distance)
else:
    distance = Borne_arrivee - Borne_depart
    print(distance)