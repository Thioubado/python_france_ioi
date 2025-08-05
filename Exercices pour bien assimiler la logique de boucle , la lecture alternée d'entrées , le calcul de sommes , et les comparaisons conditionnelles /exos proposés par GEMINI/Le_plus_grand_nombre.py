nombre_total_a_saisir = int(input())

#ligne = input()
#valeurs = ligne.split()

premier_nombre = int(input())

for _ in range(nombre_total_a_saisir - 1):
    nombre = int(input())
    if nombre > premier_nombre:
        premier_nombre = nombre
print(premier_nombre)