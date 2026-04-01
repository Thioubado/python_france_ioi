# Concours de tir à la corde
"""nombre_de_membre = int(input())
result = 0
resultat = 0
for _ in range(nombre_de_membre):
    for i in range(nombre_de_membre):
        poids = int(input())
        result += poids
    #print("poids total equipe 1 : ",result)
    for j in range(nombre_de_membre):
        poids = int(input())
        resultat += poids
    #print("poids total equipe 2 : ",resultat)
    if result > resultat:
        print("L'équipe 1 a un avantage")
        print("poids total equipe 1 : ",result)
    else:
        print("L'équipe 2 a un avantage")
        print("poids total equipe 2 : ",resultat)"""

nombre_de_membre = int(input())
equipe_1 = 0
equipe_2 = 0

for i in range(1,nombre_de_membre * 2 + 1):
    poids = int(input())
    if i % 2 == 1:
        equipe_1 += poids
    else:
        equipe_2 += poids
if equipe_1 > equipe_2:
    print("L'équipe 1 a un avantage")
else:
    print("L'équipe 2 a un avantage")

print("Poids total pour l'équipe 1 :", equipe_1)
print("Poids total pour l'équipe 2 :", equipe_2)
