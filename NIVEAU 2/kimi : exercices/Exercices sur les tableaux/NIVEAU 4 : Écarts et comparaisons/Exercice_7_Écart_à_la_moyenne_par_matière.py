# Exercice 7 : Écart à la moyenne par matière
nbre_d_eleves = int(input())

nbre_de_matieres = int(input())

liste_des_eleves = []

for eleve in range(nbre_d_eleves):
    liste_des_notes = []
    for matiere in range(nbre_de_matieres):
        notes = float(input())

        # liste_des_notes += [notes]
        liste_des_notes.append(notes)
    liste_des_eleves.append(liste_des_notes)

print(liste_des_eleves)

liste_des_moyennes = []

for matiere in range(nbre_de_matieres):
    total = 0
    for eleve in range(nbre_d_eleves):
        total += liste_des_eleves[eleve][matiere]
    # liste_des_matieres.append(total)
    moyenne = total / nbre_d_eleves
    liste_des_moyennes.append(moyenne)
print(liste_des_moyennes)

#  Étape 3 : Écarts à la moyenne

for eleve in range(nbre_d_eleves):
    for matiere in range(nbre_de_matieres):
        note = liste_des_eleves[eleve][matiere]
        moyenne_matiere = liste_des_moyennes[matiere]
        ecart = note - moyenne_matiere
        print(f"Élève {eleve + 1}, Matière {matiere + 1} : {ecart:+.2f}")