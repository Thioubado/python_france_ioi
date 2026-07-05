# Exercice 3 : Total par élève
nbre_d_eleves  = int(input())

nbre_de_matieres = int(input())

liste_des_eleves = []

for i in range(nbre_d_eleves):
    liste_des_notes = []
    for matiere in range(nbre_de_matieres):
        notes = float(input())

        #liste_des_notes += [notes]
        liste_des_notes.append(notes)

    liste_des_eleves.append(liste_des_notes)

    #moyenne = liste_des_notes / nbre_de_matieres

print(liste_des_eleves)

liste_des_moyennes = []
for matiere in range(nbre_de_matieres):
    total = 0
    for eleve in range(nbre_d_eleves):
        total += liste_des_eleves[eleve][matiere]

    moyenne = total / nbre_d_eleves
    liste_des_moyennes.append(moyenne)
print(liste_des_moyennes)