nombre_de_voitures = int(input())

ligne = input()
valeurs = ligne.split()

modele_premiere_voiture = valeurs[0]
vitesse_premiere_voiture = int(valeurs[1])

for _ in range(nombre_de_voitures - 1):
    ligne = input()
    valeurs = ligne.split()
    modele = valeurs[0]
    vitesse = int(valeurs[1])
    if vitesse > vitesse_premiere_voiture:
        vitesse_premiere_voiture = vitesse
        modele_premiere_voiture = modele
print(f"La voiture la plus rapide est la Modèle {modele_premiere_voiture} avec une vitesse de {vitesse_premiere_voiture}")