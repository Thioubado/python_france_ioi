# Exercice 3 : Le dernier état connu
villes =[0, 0, 0]

nbre_relevés = int(input())

for i in range(nbre_relevés):
    numero_ville = int(input())
    temperature = int(input())

    numero_ville -= 1

    #villes[numero_ville] += temperature
    villes[numero_ville] = temperature

# len(villes) donne la taille du tableau (ici 3)
# range(len(villes)) va donc générer les nombres 0, 1, 2
for i in range(len(villes)):
    # i est l'indice. Pour avoir le numéro de la ville, on fait i + 1
    # Pour avoir la température, on regarde dans le tableau : villes[i]
    print(f'{i + 1} : {villes[i]}')