# Exercice 1 : Notes d'élèves
liste_des_eleves = []

nbre_d_eleves = int(input())

nbre_de_matieres = int(input())

for eleves in range(nbre_d_eleves):
    notes_eleves = []
    for matiere in range(nbre_de_matieres):
        notes = float(input())
        notes_eleves += [notes]
        #notes_eleves.append(notes)
    liste_des_eleves.append(notes_eleves)

print(liste_des_eleves)
#for eleve in liste_des_eleves:
    #print(f"{eleve}")