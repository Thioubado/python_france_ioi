nombre_de_valeurs_à_lire = int(input())
compteur = False

for i in range(nombre_de_valeurs_à_lire):
    valeur = int(input())
    if valeur > 100:
        compteur = True
        valeur_trouvee = valeur
        break
if compteur:
    print(valeur_trouvee)
else:
    print("Aucun")