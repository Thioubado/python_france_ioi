# Nombre de jours dans le mois

numéro_de_mois_algoréen = int(input())

if numéro_de_mois_algoréen >= 1 and numéro_de_mois_algoréen <= 11:
    if numéro_de_mois_algoréen == 1 or numéro_de_mois_algoréen == 2 or numéro_de_mois_algoréen == 3 :
        Nombre_de_jours = 30
    elif numéro_de_mois_algoréen == 4 or numéro_de_mois_algoréen == 5 or numéro_de_mois_algoréen == 6 :
        Nombre_de_jours = 31
    elif numéro_de_mois_algoréen == 7 or numéro_de_mois_algoréen == 8 or numéro_de_mois_algoréen == 9 :
        Nombre_de_jours = 30
    elif numéro_de_mois_algoréen == 10 :
        Nombre_de_jours =31
    elif numéro_de_mois_algoréen == 11 :
        Nombre_de_jours = 29
    print(Nombre_de_jours)
else:
    print("Mois invalide")


"""
numero_mois = int(input())

if numero_mois in (1, 2, 3, 7, 8, 9):
    print(30)
elif numero_mois in (4, 5, 6, 10):
    print(31)
elif numero_mois == 11:
    print(29)
else:
    print("Mois invalide")

"""