# Exercice 3 : Notes des élèves 
eleves = [0] * 21
#notes = [0] *20

nbre_eleves = int(input())

for i in range(nbre_eleves):
    note = int(input())

    eleves[note] += 1

for i in eleves:
    print(i)