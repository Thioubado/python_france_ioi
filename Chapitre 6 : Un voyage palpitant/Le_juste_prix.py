# Le juste prix

nbre_marchands = int(input())

prix_1 = int(input())

position_1 = 1

for i in range(2, nbre_marchands + 1):
    prix = int(input())

    if prix < prix_1 :
        prix_1 = prix
        position_1 = i
    elif prix == prix_1 :
        prix_1 = prix 
        position_1 = i
    
print(position_1)
