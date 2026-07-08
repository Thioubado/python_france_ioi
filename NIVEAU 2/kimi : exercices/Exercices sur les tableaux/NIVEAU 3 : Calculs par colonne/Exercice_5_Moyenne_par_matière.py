# Exercice 5 : Moyenne par matière
nbre_d_eleves = int(input())

nbre_de_matieres = int(input())

liste_des_eleves= []

for eleve in range(nbre_d_eleves):
    liste_des_notes = []
    for matiere in range(nbre_de_matieres):
        notes = int(input())

        # Mettre les notes dans un tableau(liste)
        #liste_des_notes += [notes]
        liste_des_notes.append(notes)
    liste_des_eleves.append(liste_des_notes)

print(liste_des_eleves)

liste_des_matieres = []

for matiere in range(nbre_de_matieres):
    total = 0
    for eleve in range(nbre_d_eleves):
        total += liste_des_eleves[eleve][matiere]

    moyenne = total / nbre_d_eleves
    liste_des_matieres.append(moyenne)
    
print(liste_des_matieres)

