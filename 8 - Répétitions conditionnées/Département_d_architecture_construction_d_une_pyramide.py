# Département d'architecture : construction d'une pyramide
budget = int(input())
hauteur = 0
pierres_utilisees = 0

while True:
    prochain_etage = (hauteur + 1)**2
    
    if pierres_utilisees + prochain_etage <= budget:
        pierres_utilisees += prochain_etage
        hauteur += 1
    else:
        break
print(hauteur)
print(pierres_utilisees)