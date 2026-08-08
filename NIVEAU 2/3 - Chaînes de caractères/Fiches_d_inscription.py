# Fiches d’inscription
nbPersonnes = int(input())


for personne in range(nbPersonnes):
    identite = input()

    identite = identite.split()

    prenom = identite[0]
    nom = identite[1]

    print(f"{nom} {prenom}")