# Exercice 1 — Palindrome de nombres
nombre = int(input())

tableau_des_chiffres = []
for i in range(nombre):
    chiffre = int(input())
    #tableau_des_chiffres += [chiffre]
    tableau_des_chiffres.append(chiffre)

est_palindrome = True
for i in range(nombre // 2):
    if tableau_des_chiffres[i] != tableau_des_chiffres [nombre -1 - i]:
        est_palindrome = False
#print(est_palindrome)

if est_palindrome == True:
    print("OUI")
else:
    print("NON")










"""
Exercice 1 — Palindrome de nombres
Lis un nombre N, puis N entiers. Affiche "OUI" si la séquence est un palindrome (elle se lit pareil à l'endroit et à l'envers), sinon "NON".

Compétence travaillée : comparer un tableau avec sa version inversée.

"""