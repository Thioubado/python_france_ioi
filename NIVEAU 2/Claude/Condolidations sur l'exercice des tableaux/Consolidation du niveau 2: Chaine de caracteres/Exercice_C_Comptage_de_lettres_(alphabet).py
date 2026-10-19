# Exercice C — Comptage de lettres (alphabet)
compteur = [0] * 26

alphabet = "abcdefghijklmnopqrstuvwxyz"

nombre_de_phrase = int(input())

for ligne in range(nombre_de_phrase):
    phrase = input().lower()

    for lettre in phrase:
        if (lettre in alphabet):
            position = alphabet.index(lettre)
            compteur[position] += 1

for i in range(len(compteur)):
    if compteur[i] != 0:
        print(alphabet[i], ":", compteur[i])