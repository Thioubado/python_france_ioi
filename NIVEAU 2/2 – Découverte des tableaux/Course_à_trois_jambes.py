# Course à trois jambes
nombre_de_participants = int(input())

liste_des_particpants = []
for participant in range(nombre_de_participants):
    choix = int(input())

    #liste_des_particpants += [choix]
    liste_des_particpants.append(choix)

liste_des_particpants.sort()
#print(liste_des_particpants)


for i in range(nombre_de_participants // 2):
    print(liste_des_particpants[i], liste_des_particpants[nombre_de_participants - 1 - i])