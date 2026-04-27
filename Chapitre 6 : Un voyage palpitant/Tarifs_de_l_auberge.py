# https://www.france-ioi.org/algo/task.php?idChapter=647&idTask=1948

age = int(input())
poids_des_bagages = int(input())

if age == 60:
    print(0)
elif age < 10:
    prix = 5
    print(prix)
else:
    prix = 30
    if poids_des_bagages >= 20:
        prix = prix + 10
    print(prix)