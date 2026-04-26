# https://www.france-ioi.org/algo/task.php?idChapter=647&iOrder=4

nombre_de_montées_et_descentes = int(input())

total_montee = 0
total_descente = 0
for i in range(nombre_de_montées_et_descentes):
    variation = int(input())
    if variation > 0:
        total_montee = total_montee + variation
    else: 
        total_descente = total_descente + abs( variation)
print(total_montee)
print(total_descente)

