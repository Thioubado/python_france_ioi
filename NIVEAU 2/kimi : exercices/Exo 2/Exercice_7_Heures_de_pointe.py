# Exercice 7 : Heures de pointe
nbre_d_heures = [0] * 24

nbre_de_releves = int(input())

for i in range(nbre_de_releves):
    heure = int(input())
    nombre_voitures = int(input())

    nbre_d_heures[heure] += nombre_voitures

max_voiture = 0
heure_max = 0

for i in range(len(nbre_d_heures)):
    if nbre_d_heures[i] > max_voiture:
        max_voiture = nbre_d_heures[i]
        heure_max = i

print(f"{heure_max} : {max_voiture}")