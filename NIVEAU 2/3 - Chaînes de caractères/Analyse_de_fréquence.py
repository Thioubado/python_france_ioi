# Analyse de fréquence
compteur_longueurs = [0] * (100 + 1)
nbLignes,nbMots = map(int, input().split())
#print(nbLignes,nbMots)
for ligne in range(nbLignes):
    phrase = input().split()

    #for i in range(len(phrase)):
    for mot in phrase:
        mot = len(mot)
        compteur_longueurs[mot] += 1

for i in range(len(compteur_longueurs)):
    if compteur_longueurs[i] != 0:
        print(i, ":", compteur_longueurs[i])