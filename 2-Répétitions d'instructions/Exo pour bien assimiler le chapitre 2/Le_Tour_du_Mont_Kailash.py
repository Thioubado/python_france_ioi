from robot import *

for tour in range(108):
    for _ in range(13):
        haut()
    for _ in range(13):
        droite()
    for _ in range(13):
        bas()
    for _ in range(13):
        gauche()
