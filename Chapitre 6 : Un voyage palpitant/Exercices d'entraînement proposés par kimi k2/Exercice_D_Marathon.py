# Exercice D : Marathon

nbre_coureurs = int(input())

temps1 = int(input())

min = temps1
max = temps1

for _ in range(nbre_coureurs - 1):
    temps = int(input())
    if temps < min :
        min = temps
    
    if temps > max :
        max = temps

ecart = max - min
print(min)
print(max)
print(ecart)
