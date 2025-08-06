liste_de_nombres_entiers = input()
valeurs = liste_de_nombres_entiers.split()

meilleur_nombre = int(valeurs[0])

for valeur in valeurs:
    premier_nombre = int(valeur)
    if abs(premier_nombre) < abs(meilleur_nombre):
        meilleur_nombre = premier_nombre
    elif abs(premier_nombre) == abs(meilleur_nombre) and premier_nombre > meilleur_nombre:
        meilleur_nombre = premier_nombre
print(meilleur_nombre)