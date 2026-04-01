# Traversée du pont
"""dé_1 = int(input())
dé_2 = int(input())

if 0 < dé_1 < 7 or 0 < dé_2 < 7 :
    if dé_1 + dé_2 >= 10:
        somme = dé_1 + dé_2
        print("Taxe spéciale !")
        print(36)
    elif dé_1 + dé_2 < 10 :
        somme = (dé_1 + dé_2) * 2
        print("Taxe régulière")
        print(somme)
else:
    print("le chiffre choisit pour chaue dé doit etre copmris entre 1 et 6")"""

dé_1 = int(input())
dé_2 = int(input())
somme = dé_1 + dé_2

if somme >= 10 :
    print("Taxe spéciale !")
    print(36)
else:
    print("Taxe régulière")
    print(somme * 2)