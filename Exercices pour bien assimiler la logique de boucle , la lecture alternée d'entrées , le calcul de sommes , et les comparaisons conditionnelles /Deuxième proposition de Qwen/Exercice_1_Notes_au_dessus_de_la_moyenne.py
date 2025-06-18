nombre_d_élèves = int(input())
élèves_avec_moyenne = 0 
for i in range(nombre_d_élèves):
    notes = int(input())
    if notes >= 10:
        élèves_avec_moyenne += 1
print(élèves_avec_moyenne)