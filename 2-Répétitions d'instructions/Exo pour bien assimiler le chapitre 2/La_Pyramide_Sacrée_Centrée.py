for ligne in range(10):
    for espace in range(10 - 1 - ligne):
        print(" ", end="")
    for caractere in range(ligne * 2 + 1 ):
        print("#", end="")
    print()