# Exercice E : Boîte aux lettres

nbre_maisons = int(input())

position_1 = int(input())

position_1_gauche = position_1
position_1_droite = position_1

for _ in range(nbre_maisons - 1):
    position = int(input())

    if position < position_1_gauche :
        position_1_gauche = position

    if position > position_1_droite :
        position_1_droite = position
    
distance = position_1_droite - position_1_gauche
print(distance)