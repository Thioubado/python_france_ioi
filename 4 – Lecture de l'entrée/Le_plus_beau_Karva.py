# Le plus beau Karva
nombre_de_Karvas_en_compétition = int(input())
for element in range(nombre_de_Karvas_en_compétition):
    son_poids = int(input())
    son_âge = int(input())
    la_longueur_de_ses_cornes = int(input())
    la_hauteur_au_garrot  = int(input())
    sa_note = (la_longueur_de_ses_cornes * la_hauteur_au_garrot) + son_poids
    print(sa_note)