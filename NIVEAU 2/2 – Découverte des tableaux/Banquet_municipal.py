# Banquet municipal

nombre_total_de_positions = int(input())

nombre_de_changements_de_positions = int(input())

tableau_position = []
for position in range(nombre_total_de_positions):
    numero = int(input())

    #tableau_position += numero
    tableau_position.append(numero)
#print(tableau_position)

for changement in range(nombre_de_changements_de_positions):
    position1 = int(input())
    position2 = int(input())

    temp = tableau_position[position1]
    tableau_position[position1] = tableau_position[position2]
    tableau_position[position2] = temp

for i in tableau_position:
    print(i)