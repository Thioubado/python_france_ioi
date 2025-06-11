premier_dé = int(input())
deuxieme_dé = int(input())
Taxe_spéciale = "Taxe spéciale !"
Taxe_régulière = "Taxe régulière"

somme = premier_dé + deuxieme_dé
if somme >= 10 :
    print(Taxe_spéciale)
    print(36)
else:
    somme = (premier_dé + deuxieme_dé) * 2
    print(Taxe_régulière)
    print(somme)