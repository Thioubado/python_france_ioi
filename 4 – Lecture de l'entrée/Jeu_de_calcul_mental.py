"""unNombreAuChoix = int(input())
nombre_de_base = 66
for i in range(unNombreAuChoix):
    personne_1 = nombre_de_base * 2
    personne_2 = personne_1 * 3
    personne_3 = personne_2 * 4
print(nombre_de_base)
print(personne_1)
print(personne_2)
print(personne_3)"""

unNombreAuChoix = int(input())
nombre_de_base = 66
print(nombre_de_base)
for i in range(2, unNombreAuChoix + 1):
    nombre_de_base = nombre_de_base * i
    print(nombre_de_base)