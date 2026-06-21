# Exercice 5 : Banque

client = [0] * 10

nombre_d_opérations = int(input())

for i in range(nombre_d_opérations):
    numero_client = int(input())
    montant = int(input())

    index = numero_client - 1

    if montant > 0:
        client[index] += montant
    else:
        if montant < 0:
            if client[index] + montant >= 0:
                client[index] += montant

for solde in client:
    print(solde)