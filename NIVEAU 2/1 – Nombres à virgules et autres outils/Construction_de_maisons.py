# Construction de maisons
from math import *
quantite_ciment = float(input())
poids_sac_ciment = 60
prix_sac_ciment = 45

cout = ceil(quantite_ciment / poids_sac_ciment) * prix_sac_ciment
print(cout)