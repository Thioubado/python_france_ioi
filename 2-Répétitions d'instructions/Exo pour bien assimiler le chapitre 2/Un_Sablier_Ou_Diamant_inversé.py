'''for ligne in range(10):
    for colonne in range(10 - ligne + 1):
        print("#", end="")
    print()
for ligne in range(10):
    for colonne in range(ligne + 2):
        print("#", end="")
    print()'''
for ligne in range(5):
    for espace in range(ligne):
        print(" ", end="")
    for colonne in range((5 - ligne) * 2):
        print("#", end="")
    print()
for ligne in range(5):
    for espace in range(4 - ligne):
        print(" ", end="")
    for colonne in range((ligne + 1) * 2):
        print("#", end="")
    print()

'''for ligne in range(10):
    for colonne in range(ligne + 1):
        print("#", end="")
    print()'''