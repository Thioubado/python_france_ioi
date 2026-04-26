# https://www.france-ioi.org/algo/task.php?idChapter=647&iOrder=3

# solution 1
nombre_de_jours_de_marche = int(input())
distance_maximale = 0
for i in range(nombre_de_jours_de_marche):
    distance_parcourue = int(input())
    if distance_parcourue > distance_maximale:
        distance_maximale = distance_parcourue
print(distance_maximale) 

# Solution 2
joursDeMarche = int(input())
distanceMax = int(input())

for i in range(joursDeMarche - 1):
    distanceParJour = int(input())
    if distanceParJour > distanceMax:
        distanceMax = distanceParJour
print(distanceMax)