# Transport des bagages
Transport_des_bagages = int(input())
poids_d_un_paquet = int(input())

poids_total = int(Transport_des_bagages * poids_d_un_paquet)
if poids_total > 105:
    print("Surcharge !")