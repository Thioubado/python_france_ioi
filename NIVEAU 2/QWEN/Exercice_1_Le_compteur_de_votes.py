# Exercice 1 : Le compteur de votes
candidats = [0, 0, 0, 0]

nombre_de_votes = int(input())

for i in range(nombre_de_votes):
    vote = int(input())
    vote = vote - 1
    candidats[vote] = candidats[vote] + 1
#print(candidats)

for i in candidats:
   print(i)