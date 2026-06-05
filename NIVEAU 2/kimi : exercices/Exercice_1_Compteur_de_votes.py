# Exercice 1 : Compteur de votes
liste_candidat = [0] * 10

nombre_de_votes = int(input())

for i in range(nombre_de_votes):
    vote_pour_candidat = int(input())
    index = vote_pour_candidat - 1
    liste_candidat[index] += 1 

"""for vote_pour_candidat in liste_candidat:
    print(vote_pour_candidat)"""

for i in range(10):
    print(liste_candidat[i])