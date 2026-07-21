# Exercice 4 — Décodage César
nombre = int(input())

liste_des_nombres = []
for i in range(nombre):
    chiffre = int(input())
    #liste_des_nombres += chiffre
    liste_des_nombres.append(chiffre)


for j in range(nombre):

    if liste_des_nombres[j] - 3 < 1:
        resultat = liste_des_nombres[j] - 3 + 26
    else:
        resultat = liste_des_nombres[j] - 3

    print(resultat)