# Journée des cadeaux
nombre_d_habitants  = int(input())

liste_des_fortunes = []
for habitant in range(nombre_d_habitants):
    fortune = int(input())

    #liste_des_fortunes += fortune
    liste_des_fortunes.append(fortune)

liste_des_fortunes.sort()

if nombre_d_habitants % 2 == 0:
    result = float((liste_des_fortunes[(nombre_d_habitants// 2) - 1] + liste_des_fortunes[nombre_d_habitants // 2]) / 2)
else:
    result = liste_des_fortunes[nombre_d_habitants // 2]

print(result)