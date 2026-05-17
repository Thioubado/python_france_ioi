# Administration : comptes annuels
"""somme = 0
montant = int(input())

while montant != -1:
    somme += montant
    montant = int(input())
print(somme)"""

somme = 0

while True:
    montant = int(input())
    if montant == -1 :
        break
    somme = somme + montant
print(somme)