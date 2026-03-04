"""for _ in range(20):
    for _ in range(20):
        print("O", end=(""))
        print("X", end=(""))
    print()
 
"""
for ligne in range(40):
    for colonne in range(40):
        if (ligne + colonne) % 2 == 0:
            print("O", end="")
        else:
            print("X", end="")
    print()