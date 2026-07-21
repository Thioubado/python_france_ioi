# Exercice 3 — Somme des extrêmes

nombre = int(input())

liste_des_nombres = []
for i in range(nombre):
    chiffre = int(input())
    #liste_des_nombres += [chiffre]
    liste_des_nombres.append(chiffre)



for j in range(nombre // 2):
    print(liste_des_nombres[j] + liste_des_nombres[nombre -1 - j])

















"""
Exercice 3 — Somme des extrêmes
Lis un tableau de N entiers. Calcule et affiche la somme du premier et du dernier élément, puis du deuxième et de l'avant-dernier, et ainsi de suite (comme si tu repliais le tableau en deux).

Compétence travaillée : manipuler deux indices en même temps, un qui avance et un qui recule.
"""