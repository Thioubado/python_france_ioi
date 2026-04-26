# https://www.france-ioi.org/algo/task.php?idChapter=647&iOrder=1

le_nombre_de_lieux = int(input())
nbre_de_villes = 0
for i in range(le_nombre_de_lieux):
    nombre_de_gens = int(input())
    if nombre_de_gens > 10000:
        nbre_de_villes += 1
print(nbre_de_villes)