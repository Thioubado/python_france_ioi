# Exercice 9 : Meilleur et pire élève

nombre_d_eleves = int(input())

nombre_de_matieres = int(input())

# Creation de la liste des eleves
liste_des_eleves = []

for eleve in range(nombre_d_eleves):
    liste_des_notes = []
    for matiere in range(nombre_de_matieres):
        notes = float(input())

        liste_des_notes.append(notes)

    liste_des_eleves.append(liste_des_notes)

print(liste_des_eleves)

# Creation de la liste des moyennes matieres et des totaux
# ============================================
# Étape 2 : MOYENNES PAR MATIÈRE (vous l'avez)
# ============================================
liste_des_totaux = []
liste_des_moyennes = []

for matiere in range(nombre_de_matieres):
    total = 0
    for eleve in range(nombre_d_eleves):
        total += liste_des_eleves[eleve][matiere]
    moyenne = total / nombre_d_eleves

    liste_des_totaux.append(total)
    liste_des_moyennes.append(moyenne)

print(liste_des_totaux)
print(liste_des_moyennes)

# ============================================
# Étape 3 : MOYENNES PAR ÉLÈVE (il manquait !)
# ============================================

liste_des_moyennes_par_eleve = []
for eleve in range(nombre_d_eleves):
    #total += liste_des_eleves[eleve]
    total_des_notes_par_eleve = sum(liste_des_eleves[eleve])
    moyenne_eleve = total_des_notes_par_eleve / nombre_de_matieres
    liste_des_moyennes_par_eleve.append(moyenne_eleve)
print("Moyennes par élève :", liste_des_moyennes_par_eleve)

# ============================================
# Étape 4 : MEILLEUR ET PIRE ÉLÈVE
# ============================================
meilleure_moyenne = max(liste_des_moyennes_par_eleve)
pire_moyenne = min(liste_des_moyennes_par_eleve)

index_meilleure_moyenne = liste_des_moyennes_par_eleve.index(meilleure_moyenne)
index_pire_moyenne = liste_des_moyennes_par_eleve.index(pire_moyenne)

print(f"\nMeilleur eleve: Eleve {index_meilleure_moyenne + 1} avec {meilleure_moyenne:.2f}")

print(f"\nPire eleve: Eleve {index_pire_moyenne + 1} avec {pire_moyenne:.2f}")


# ============================================
# Étape 5 : MEILLEURE NOTE PAR MATIÈRE
# ============================================
print("\nMeilleures notes par matière :")
for matiere in range(nombre_de_matieres):
    #Creation de la liste des notes pour toutes les matieres
    liste_des_notes_de_toutes_matieres = []
    for eleve in range(nombre_d_eleves):
        liste_des_notes_de_toutes_matieres.append(liste_des_eleves[eleve][matiere])

    meilleure_note = max(liste_des_notes_de_toutes_matieres)

    index_meilleure_note = liste_des_notes_de_toutes_matieres.index(meilleure_note)

    print(f"    Matiere:{matiere + 1} : {meilleure_note} (Eleve {index_meilleure_note + 1})")

# ============================================
# Étape 6 : NOTE LA PLUS FAIBLE DU TABLEAU
# ============================================
toutes_les_notes = []
for eleve in range(nombre_d_eleves):
    for matiere in range(nombre_de_matieres):
        toutes_les_notes.append(liste_des_eleves[eleve][matiere])
    
note_min = min(toutes_les_notes)
print(f"\nNote la plus faible : {note_min}")
 


"""
Même entrée que l'exercice 1.
Trouver :
- L'élève avec la meilleure moyenne générale
- La meilleure note dans chaque matière
- La note la plus faible du tableau
"""