nombre_de_membres_par_équipe = int(input())
total_equipe_1 = 0
total_equipe_2 = 0

for i in range(nombre_de_membres_par_équipe * 2):
    poids = int(input())
    if i % 2 == 0:
        total_equipe_1 = total_equipe_1 + poids
    else:
        total_equipe_2 = total_equipe_2 + poids
if total_equipe_1 > total_equipe_2:
    print("L’équipe 1 a un avantage")
    print("Poids total pour l’équipe 1 :", total_equipe_1)
    print("Poids total pour l’équipe 2 :", total_equipe_2)
else:
    print("L’équipe 2 a un avantage")
    print("Poids total pour l’équipe 1 :", total_equipe_1)
    print("Poids total pour l’équipe 2 :", total_equipe_2)
