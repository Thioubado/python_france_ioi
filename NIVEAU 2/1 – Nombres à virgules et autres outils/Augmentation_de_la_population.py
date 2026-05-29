# Augmentation de la population
from math import *
population = int(input())
taux_croissance = float(input())

nouvelle_population = floor(population * (1 + taux_croissance / 100))


print(nouvelle_population)