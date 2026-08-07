# Résumés de livres

nbLivres = int(input())

longueurMinimale = int(input())

for livre in range(nbLivres):
    titre = input()
    résumé = input()

    if len(résumé) < longueurMinimale:
        print(titre)