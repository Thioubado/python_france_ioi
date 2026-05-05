# Amitié entre gardes
date_du_début_soldat_1 = int(input())
date_de_fin_soldat_1 = int(input())

date_du_début_soldat_2 = int(input())
date_de_fin_soldat_2 = int(input())


if date_du_début_soldat_2 <= date_de_fin_soldat_1 and date_du_début_soldat_1 <= date_de_fin_soldat_2:
    print("Amis")
else:
    print("Pas amis")