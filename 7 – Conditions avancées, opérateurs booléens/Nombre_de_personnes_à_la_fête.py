# Nombre de personnes à la fête
nbPersonnes = int(input())

present = 0
max_present = 0

for i in range(2 * nbPersonnes):
    evenement = int(input())

    if evenement > 0 :
        present += 1
    else:
        present -= 1
    
    if present > max_present :
        max_present = present
print(max_present)