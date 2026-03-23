"""droite = 0
gauche = 0
for l in range(1, 11):
    for anneaux in range(l):
        droite += 1
        print(f"droite {l}")
    print("ramasser")"""

for i in range(1,11):
    for _ in range(i):
        droite()
    ramasser()
    for _ in range(i):
        gauche()
    deposer()

