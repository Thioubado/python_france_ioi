# Exercice 4 — Plusieurs paires d'intervalles

nbre_de_paires = int(input())


for i in range(nbre_de_paires):
    a1 = int(input())
    b1 = int(input())

    a2 = int(input())
    b2 = int(input())

    if a1 < b2 and a2 < b1 :
        print("OUI")
    else:
        print("NON")
