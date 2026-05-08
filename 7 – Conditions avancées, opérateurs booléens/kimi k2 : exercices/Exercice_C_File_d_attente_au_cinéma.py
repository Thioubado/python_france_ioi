# Exercice C : File d'attente au cinéma

nbre_clients = int(input())

file_d_attente = 0
personne = 0


for _ in range(2 * nbre_clients):

    evenement = int(input())

    if evenement > 0 :
        personne += 1

    if evenement < 0 :
        personne -= 1

    if personne > file_d_attente:
        file_d_attente = personne

print(file_d_attente)
