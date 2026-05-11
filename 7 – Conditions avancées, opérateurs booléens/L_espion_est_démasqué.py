# L'espion est démasqué !
nombre_de_personnes = int(input())

for i in range(nombre_de_personnes):
    taille  = int(input())
    age     = int(input())
    poids   = int(input())
    personne_avec_cheval = int(input())
    personne_cheveux_bruns = int(input())

    criteres = 0

    # test des conditions
    if taille >= 178 and taille <= 182:
        criteres += 1
    if age >= 34 :
        criteres += 1
    if poids < 70 :
        criteres += 1
    if personne_avec_cheval == 0:
        criteres += 1
    if personne_cheveux_bruns == 1:
        criteres += 1
        
    # test des criteres
    if criteres == 5 :
        print("Très probable")
    elif criteres == 4 or criteres == 3:
        print("Probable")
    elif criteres == 0:
        print("Impossible")
    else:
        print("Peu probable")





