# Exercice 1 : Élection
candidats = [0] * 10

nbre_de_votes = int(input())

for i in range(nbre_de_votes):
    #electeurs = int(input())
    vote = int(input())

    vote = vote - 1
    candidats[vote] += 1

for i in candidats:
    print(i)

"""for i in range(len(candidats)):
    print(candidats[i])"""

