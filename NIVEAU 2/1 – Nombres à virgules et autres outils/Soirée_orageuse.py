# Soirée orageuse
temps = float(input())
vitesse_du_son = 340.29 # mètres / seconde
vitesse_du_son_en_km = 1000 / vitesse_du_son

distance = round(temps / vitesse_du_son_en_km)
print(distance)