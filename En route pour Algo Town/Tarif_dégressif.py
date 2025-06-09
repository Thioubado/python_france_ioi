heure_d_arrivée = int(input())
"""print(heure_d_arrivée)"""
prix_de_base = 10
prix = prix_de_base + 5 * heure_d_arrivée
prix = min(prix, 53)
print(prix)