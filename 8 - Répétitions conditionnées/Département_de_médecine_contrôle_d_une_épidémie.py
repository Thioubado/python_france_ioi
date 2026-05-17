# Département de médecine : contrôle d'une épidémie

nbre_population = int(input())

nbre_de_malade  = 1
jour = 1 
nouveaux_malades = 0

while nbre_de_malade < nbre_population:
    nouveaux_malades = nbre_de_malade * 2
    nbre_de_malade = nbre_de_malade + nouveaux_malades
    jour += 1
print(jour)