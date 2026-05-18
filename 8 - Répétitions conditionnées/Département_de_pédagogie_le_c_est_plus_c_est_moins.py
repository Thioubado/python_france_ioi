# Département de pédagogie : le « c'est plus, c'est moins »

nombre_a_trouver = int(input())
nombre_d_essais = 0
while True:
    proposition = int(input())
    if proposition == nombre_a_trouver:
        nombre_d_essais += 1
        break
    else:
        if proposition < nombre_a_trouver:
            print("C'est plus")
            nombre_d_essais += 1
        else:
            print("C'est moins")
            nombre_d_essais += 1
print("Nombre d'essais nécessaires : ")
print(nombre_d_essais)