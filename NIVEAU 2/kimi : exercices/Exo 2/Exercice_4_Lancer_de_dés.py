# Exercice 4 : Lancer de dés
dé = [0] * 6

nbre_de_lancers = int(input())

for i in range(nbre_de_lancers):
    resultat_par_lancer = int(input())

    resultat_par_lancer -= 1

    dé[resultat_par_lancer] += 1

"""for i in dé:
    print(i)"""

for i in range(len(dé)):
    print(f"{i+1} : {dé[i]}")