# https://www.france-ioi.org/algo/task.php?idChapter=647&idTask=1943

hauteur_arbre = int(input())
nombre_de_folioles_arbre = int(input())

if hauteur_arbre <= 5 and nombre_de_folioles_arbre >= 8:
    print("Tinuviel")
elif hauteur_arbre >= 10 and nombre_de_folioles_arbre >= 10:
    print("Calaelen")
elif hauteur_arbre <= 8 and nombre_de_folioles_arbre <= 5:
    print("Falarion")
elif hauteur_arbre >= 12 and nombre_de_folioles_arbre <= 7:
    print("Dorthonion")
else:
    print("Arbre inconnu")