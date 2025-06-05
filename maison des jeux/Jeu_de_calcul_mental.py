nombre_depart = int(input())
nombre_etapes = int(input())
for i in range(nombre_etapes):
    nombre_depart = nombre_depart * (i + 1)
    print(nombre_depart)