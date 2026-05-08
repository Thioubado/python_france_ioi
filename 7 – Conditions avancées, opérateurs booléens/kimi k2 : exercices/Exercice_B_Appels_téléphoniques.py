# Exercice B : Appels téléphoniques

Appels_téléphoniques = int(input())

appel = 0
nombre_maximum_d_appels_simultanés = 0

for _ in range(Appels_téléphoniques):

    evenement = int(input())

    if evenement == 1 :
        appel += 1
    
    if evenement == -1 :
        appel -= 1

    if appel > nombre_maximum_d_appels_simultanés :
        nombre_maximum_d_appels_simultanés = appel

print(nombre_maximum_d_appels_simultanés)