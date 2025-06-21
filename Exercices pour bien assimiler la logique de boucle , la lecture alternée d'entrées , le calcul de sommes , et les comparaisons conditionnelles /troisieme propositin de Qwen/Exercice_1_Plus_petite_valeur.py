"""
🔹 Exercice 1 : Plus petite valeur
Ton programme doit :

Lire un entier : le nombre de valeurs à lire
Ensuite lire ces valeurs
Afficher la plus petite d'entre elles
Exemple :



1
2
3
4
5
6
5
12
8
15
3
9
Sortie attendue :



1
3
"""
nombre_de_valeurs_à_lire = int(input())
compteur = float('inf')
for i in range(nombre_de_valeurs_à_lire):
    valeurs = int(input())
    if valeurs < compteur:
        compteur = valeurs
print(compteur)