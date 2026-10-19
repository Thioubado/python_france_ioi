# Exercice D — Palindrome de mot

mot = input()

est_palindrome = True

for i in range(len(mot) // 2):
    if mot[i] != mot[len(mot)-1-i]:
        est_palindrome = False

if est_palindrome == True:
    print("OUI")
else:
    print("NON")