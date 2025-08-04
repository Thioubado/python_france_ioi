température_de_référence = int(input())
nombre_de_capteurs = int(input())

# Lire la premiere ligne de capteur
ligne = input()    # lit toute la ligne, ex: "5 18"
valeurs = ligne.split()          # coupe la ligne en morceaux → ['5', '18']

# Extraire les deux valeurs
position = int(valeurs[0])              # premier nombre : position
temperature = int(valeurs[1])           # deuxième nombre : température

# Initialiser avec ce premier capteur
temperature_minimum = temperature
position_plus_froide = position

# Pour les (nombre_de_capteurs - 1) capteurs restants
for _ in range(nombre_de_capteurs - 1):
    ligne = input()
    valeurs = ligne.split()
    pos = int(valeurs[0])
    temp = int(valeurs[1])
    if temp < temperature_minimum:
        temperature_minimum = temp
        position_plus_froide = pos

# Afficher la position du capteur le plus froid
print(position_plus_froide)