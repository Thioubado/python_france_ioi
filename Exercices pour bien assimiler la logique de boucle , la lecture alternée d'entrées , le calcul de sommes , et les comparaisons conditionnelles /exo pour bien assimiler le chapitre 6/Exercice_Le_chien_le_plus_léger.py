nombre_de_chiens = int(input())

ligne = input()
valeurs = ligne.split()

nom_chien_plus_leger = valeurs[0]
poids_chien_plus_leger = int(valeurs[1])

#nom = nom_chien_plus_leger
#poids = poids_chien_plus_leger

for _ in range(nombre_de_chiens - 1):
    ligne = input()
    valeurs = ligne.split()
    nom = valeurs[0]
    poids = int(valeurs[1])
    if poids < poids_chien_plus_leger:
        poids_chien_plus_leger = poids
        nom_chien_plus_leger = nom
print(nom_chien_plus_leger)