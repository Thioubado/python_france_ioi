# Personne disparue
numero_de_la_personne = int(input())
taille_liste = int(input())
trouve = False
for i in range(taille_liste):
    entiers_taille_liste = int(input())
    if numero_de_la_personne == entiers_taille_liste :
        trouve = True
        #print("Encore dans la ville")
    #else:
        #trouve
        #print("Sorti de la ville")
if trouve:
    print("Sorti de la ville")
else:
    print("Encore dans la ville")
