total = 0
case_vide = 0

for i in range(16):
    case = i + 1
    if bouse():
        ramasser()
        total += 1
        print(f"Case : {case}. Bouse trouvé : {total}.")
    else:
        case_vide +=  1
        print(f"Case: {case}. Rien {total}.")
    droite()
deposer()
print(f"Nombre_total_de_cases_parcourues = {case}")
print(f"Nombre_de_bouses_ramassées = {total}")
print(case_vide)
Pourcentage_de_cases_avec_des_bouses = (total / 16) * 100
print(Pourcentage_de_cases_avec_des_bouses)

