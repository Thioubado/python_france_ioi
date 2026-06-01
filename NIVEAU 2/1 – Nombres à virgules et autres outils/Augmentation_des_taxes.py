# Augmentation des taxes

valeur_actuelle_de_la_taxe = float(input())

valeur_de_la_nouvelle_taxe = float(input())

prix_actuel_legume = float(input())

prix_legume_sans_taxe = prix_actuel_legume / (1 + (valeur_actuelle_de_la_taxe / 100))

montant_nouvelle_taxe = (prix_legume_sans_taxe * valeur_de_la_nouvelle_taxe) / 100

prix_legume = (montant_nouvelle_taxe + prix_legume_sans_taxe)

print(round(prix_legume, 2))