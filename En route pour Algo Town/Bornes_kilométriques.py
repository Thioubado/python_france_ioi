borne_de_depart = int(input())

borne_d_arrivee = int(input())

if borne_de_depart < borne_d_arrivee :
    distance = borne_d_arrivee - borne_de_depart
    print(distance)
else:
    distance = abs(borne_de_depart - borne_d_arrivee)
    print(distance)