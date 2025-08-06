nombre_d_élèves = int(input())

premier_eleve = input()
valeur = premier_eleve.split()

nom_premier_eleve = valeur[0]
note_premier_eleve = float(valeur[1])

for _ in range(nombre_d_élèves - 1):
    eleves = input()
    valeur = eleves.split()
    nom = valeur[0]
    note = float(valeur[1])
    if note > note_premier_eleve:
        note_premier_eleve = note
        nom_premier_eleve = nom
print(nom_premier_eleve)