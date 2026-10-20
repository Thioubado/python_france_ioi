# Exercice E — Compter les mots répétés
phrase = input().split()

deja_comptes = []

compteur = 0

for mot in phrase:
    if mot not in deja_comptes and phrase.count(mot) > 1:
        #deja_comptes += deja_comptes[mot]
        deja_comptes.append(mot)
        compteur += 1
print(compteur)
