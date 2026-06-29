# Exercice 1 : Moyenne de notes 
liste_des_notes = []

nombre_eleve = int(input())
total = 0

for i in range(nombre_eleve):
    note = int(input())

    # Inserer les notes dans le tableau
    liste_des_notes = liste_des_notes + [note]

    total += note

moyenne = total / nombre_eleve

print(moyenne)