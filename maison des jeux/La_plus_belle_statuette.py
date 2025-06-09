nbre_statuettes = int(input())

for i in range(nbre_statuettes):
    poids = int(input())
    hauteur = int(input())
    volume = int(input())
    nombre_de_détails_sculptés  = int(input())
    note = (hauteur * nombre_de_détails_sculptés) + volume
    print(note)