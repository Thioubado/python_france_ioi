# Exercice 4 : Partage équitable 
groupe_d_amis = []

nbre_amis = int(input())
total = 0

for i in range(nbre_amis):
    montant_paye = float(input())

    #ajout de chaque montant au tableau
    #groupe_d_amis += [montant_paye]
    groupe_d_amis.append(montant_paye)

    #addition des montants payes
    total += montant_paye

moyenne = total / nbre_amis

for i in groupe_d_amis:
    ecart = i - moyenne
    print(f"{ecart:.1f}")