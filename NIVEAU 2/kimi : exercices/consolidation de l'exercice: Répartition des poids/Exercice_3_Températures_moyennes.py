# Exercice 3 : Températures moyennes
liste_temperature= []
total  = 0

for i in range(7):

    temperature = float(input())

    # 2 possibilites:
    # liste_temperature += [temperature] 
    liste_temperature.append(temperature)

    total += temperature

moyenne = total / len(liste_temperature)
print(f"Moyenne : {moyenne:.3f}")

for i in liste_temperature:
    difference = i - moyenne
    print(f"Ecart: {difference:+.3f}")