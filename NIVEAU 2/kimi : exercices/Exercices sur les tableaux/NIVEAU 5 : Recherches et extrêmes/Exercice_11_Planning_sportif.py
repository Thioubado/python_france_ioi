# Exercice 11 : Planning sportif

nombre_de_joueurs = int(input())

nombre_de_semaines = int(input())

tableau_planning = []

for joueur in range(nombre_de_joueurs):
    tableau_des_joueurs = []
    for semaine in range(nombre_de_semaines):
        nombre_de_minutes = int(input())

        #tableau_des_joueurs += [nombre_de_minutes]
        tableau_des_joueurs.append(nombre_de_minutes)
    tableau_planning.append(tableau_des_joueurs)

print(tableau_planning)

# ===================
# Minutes totales par joueur
# ===================
tableau_des_minutes = []
for joueur in range(nombre_de_joueurs):
    total_minutes = 0
    for semaine in range(nombre_de_semaines):
        total_minutes += tableau_planning[joueur][semaine]
    #total_minutes = sum(tableau_planning[semaine])

        tableau_des_minutes.append(total_minutes)
    
    print(f"  Joueur {joueur +1} : {total_minutes} minutes")



# ===================
# Minutes moyennes par semaine (tous joueurs confondus)
# ===================

#tableau_des_totaux = []
for semaine in range(nombre_de_semaines):
    total = 0
    for joueur in range(nombre_de_joueurs):
        total += tableau_planning[joueur][semaine]

    moyenne = total / nombre_de_joueurs

    print(f"Semaine {semaine + 1} : {moyenne:.2f}")

# ===================
# Joueur le plus utilisé
# ===================
tableau_utilisation_joueur = []
for joueur in range(nombre_de_joueurs):
    total = 0
    for semaine in range(nombre_de_semaines):
        total += tableau_planning[joueur][semaine]
    tableau_utilisation_joueur.append(total)

max_utilisation = max(tableau_utilisation_joueur)
index_max = tableau_utilisation_joueur.index(max_utilisation)

print(f"\nJoueur le plus utilisé : Joueur {index_max + 1} :  ({max_utilisation} minutes)")

# ===================
# Semaine avec le plus de minutes jouées au total
# ===================
tableau_semaine = []
for semaine in range(nombre_de_semaines):
    total = 0
    for joueur in range(nombre_de_joueurs):
        total += tableau_planning[joueur][semaine]
    tableau_semaine.append(total)

max_semaine = max(tableau_semaine)
index_semaine = tableau_semaine.index(max_semaine)

print(f"Semaine la plus chargée : Semaine {index_semaine + 1} : ({max_semaine} minutes)")





"""
Lire un nombre de joueurs et un nombre de semaines.
Pour chaque joueur et chaque semaine, lire : minutes jouées.
Afficher :
- Minutes totales par joueur
- Minutes moyennes par semaine (tous joueurs confondus)
- Joueur le plus utilisé
- Semaine avec le plus de minutes jouées au total

"""