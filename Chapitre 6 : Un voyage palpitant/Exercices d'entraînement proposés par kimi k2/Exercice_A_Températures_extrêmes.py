# Exercice A : Températures extrêmes

nbre_de_jours = int(input())

températures1 = int(input())
#températures_négatives = int(input())
min_temperature = températures1
max_temperature = températures1

for i in range(nbre_de_jours - 1):
    temperature = int(input())
    if temperature < min_temperature:
        min_temperature = temperature
    
    if temperature > max_temperature:
        max_temperature = temperature
print(f"min: {min_temperature}°C")
print(f"max: {max_temperature}°C")

