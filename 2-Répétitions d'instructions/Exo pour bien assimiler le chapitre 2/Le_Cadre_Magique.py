for ligne in range(15):
    for colonne in range(30):
        if ligne == 0 or ligne == 14 or colonne == 0 or colonne == 29: 
            print("#", end="")
        else:
            print(" ", end="")
    print()