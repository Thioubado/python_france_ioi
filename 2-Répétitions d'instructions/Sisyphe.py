from robot import *

for i in range(21):
    haut()
    droite()
    print(f"Marche {i + 1} atteinte")

for i in range(21):
    gauche()
    bas()
    print(f"Marche {21 - i} atteinte")
