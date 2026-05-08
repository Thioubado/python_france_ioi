# Exercice A : Capacité du parking
capacité_limitée = int(input())

voiture_present = 0
nbre_max_voitures = 0

for i in range(capacité_limitée):
    mouvement = int(input())

    if mouvement == 1 or mouvement == -1 :
        if mouvement == 1 :
            voiture_present += 1

        if mouvement == -1 :
            voiture_present -= 1
        
        if voiture_present > nbre_max_voitures :
            nbre_max_voitures = voiture_present

print(nbre_max_voitures)