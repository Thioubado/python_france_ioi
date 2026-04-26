# https://www.france-ioi.org/algo/task.php?idChapter=647&idTask=1945

position_actuelle = int(input())

nombre_de_villages = int(input())

nbreDeVillageA50Km = 0
for i in range(nombre_de_villages):
    position_de_chaque_village = int(input())
    if abs(position_actuelle - position_de_chaque_village) <= 50:
        nbreDeVillageA50Km += 1
print(nbreDeVillageA50Km)