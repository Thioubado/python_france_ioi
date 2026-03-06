"""for ligne in range(5):
    for colonne in range(10):
        if ligne == 0:
            print("#", end="")
        else:
            ligne -= 1
    print()"""


"""for ligne in range(10):
    for colonne in range(10):
        if ligne == 9:
            print("#", end="")
        else :
            ligne += 1
    print()"""

for ligne in range(10):
    for colonne in range(ligne + 1):
        print("#", end="")
    print()