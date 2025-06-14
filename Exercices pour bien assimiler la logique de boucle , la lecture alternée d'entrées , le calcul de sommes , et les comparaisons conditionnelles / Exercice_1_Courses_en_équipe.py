"""
🧩 Exercice 1 : Courses en équipe
Ton programme doit :

Lire un entier : le nombre de courses.
Ensuite lire deux temps par course (un pour chaque équipe).
Calculer la somme des temps pour chaque équipe.
Afficher l’équipe gagnante (celle avec le temps total le plus petit ).
Exemple :



1
2
3
4
5
6
7
3
10
12
8
9
11
7
Sortie attendue :



1
2
3
L'équipe 2 a gagné
Temps total équipe 1 : 29
Temps total équipe 2 : 28

"""
nbre_de_courses = int(input())
equipe_1 = 0
equipe_2 = 0
for i in range(nbre_de_courses * 2):
    temps = int(input())
    if i % 2 == 0:
        equipe_1 = equipe_1 + temps
    else:
        equipe_2 = equipe_2 + temps
if equipe_1 < equipe_2:
    print("L'équipe 1 a gagné")
else:
    print("L'équipe 2 a gagné")
print("Temps total équipe 1 :", equipe_1)
print("Temps total équipe 2 :", equipe_2)