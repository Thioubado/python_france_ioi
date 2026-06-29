# Exercice 2 : Écart à la moyenne
liste_des_eleves = []
total = 0
nbre_eleve = int(input())

for i in range(nbre_eleve):
    note = float(input())

    #liste_des_eleves.append(note)
    liste_des_eleves += [note]
    total += note

moyenne = total / nbre_eleve

for i in liste_des_eleves:
    difference = moyenne - i
    print(difference)