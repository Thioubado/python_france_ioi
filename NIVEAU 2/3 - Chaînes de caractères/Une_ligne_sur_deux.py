# Une ligne sur deux 

nbre_de_lignes = int(input())


for ligne in range(nbre_de_lignes):
    phrase = input()

    if ligne % 2 == 0:
        print(phrase)

