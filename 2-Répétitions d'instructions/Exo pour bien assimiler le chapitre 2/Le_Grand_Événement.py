#Le Grand Événement

'''
from robot import *

for ligne in range(10):
    if ligne % 2 == 0:
        for colonne in range(9):
            droite()
    else:
        for colonne in range(9):
            gauche()
    if ligne < 9 :
        haut()
for _ in range(9):
    bas()

'''

'''from robot import *

# Parcourir les 10 colonnes
for colonne in range(10):
    
    # Colonne paire : monter
    if colonne % 2 == 0:
        for _ in range(9):
            haut()
    
    # Colonne impaire : descendre
    else:
        for _ in range(9):
            bas()
    
    # Aller à la colonne suivante (sauf après la dernière)
    if colonne < 9:
        droite()

# Retour au point de départ (en haut à droite → aller à gauche)
for _ in range(9):
    gauche()
'''


'''

from robot import *
for loop in range(9):
   haut()
for loop in range(9):
   droite()
bas()
for loop in range(8):
   gauche()
bas()
for loop in range(8):
   droite()
bas()
for loop in range(8):
   gauche()
bas()
for loop in range(8):
   droite()
bas()
for loop in range(8):
   gauche()
bas()
for loop in range(8):
   droite()
bas()
for loop in range(8):
   gauche()
bas()
for loop in range(8):
   droite()
bas()
for loop in range(9):
   gauche()

'''

L = 10
for colonne in range(L):
   if colonne % 2 == 0:
      for _ in range(L - 1):
         haut()  
   else:
      for _ in range(L - 1):
         bas()
   if colonne < L-1:
      droite()
   for _ in range(L - 1):
      gauche()
   
