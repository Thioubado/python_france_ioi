# Département de chimie : mélange explosif
"""
nombre_total_de_mesures = int(input())

temperature_minimale = int(input())

temperature_maximale = int(input())

for _ in range(nombre_total_de_mesures):
    temperatures_releves = int(input())

    if temperature_minimale <= temperatures_releves <= temperature_maximale:
        print("Rien à signaler")
    else:
        print("Alerte !!")
        break
"""

# solution 2
nombre_total_de_mesures = int(input())

temperature_minimale = int(input())

temperature_maximale = int(input())

compteur = 0

while compteur < nombre_total_de_mesures:
    temperatures_releves = int(input())
    compteur += 1

    if temperature_minimale <= temperatures_releves <= temperature_maximale:
        print("Rien à signaler")
    else:
        print("Alerte !!")
        break
