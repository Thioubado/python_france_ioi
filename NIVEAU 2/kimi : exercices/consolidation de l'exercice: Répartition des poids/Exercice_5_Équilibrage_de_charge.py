# Exercice 5 : Équilibrage de charge
liste_d_ordinateurs = []

nbre_d_ordinateurs = int(input())
total_charge_actuelle = 0

for i in range(nbre_d_ordinateurs):
    charge_actuelle = int(input())
    #liste_d_ordinateurs += [charge_actuelle]
    liste_d_ordinateurs.append(charge_actuelle)
    #totalite des charges actuelles
    total_charge_actuelle += charge_actuelle

nouvelles_tâches_à_répartir = int(input())

moyenne = (total_charge_actuelle + nouvelles_tâches_à_répartir) / nbre_d_ordinateurs

print(f"charge idéale : {moyenne:.1f}")

for i in liste_d_ordinateurs:
    ecart = moyenne - i
    print(f"{ecart:+.0f}") 