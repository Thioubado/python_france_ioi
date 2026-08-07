# Lire ou ne pas lire, telle est la question
nbLivres = int(input())

longueur_max_lue = 0
for livre in range(nbLivres):
    titre = input()

    if len(titre) > longueur_max_lue:
        longueur_max_lue = len(titre)
        print(titre)