# Exercice B : Meilleur et pire score
nbre_eleve = int(input())

note = int(input())

meilleure_note = note
pire_note = note

total = note

for i in range(nbre_eleve - 1):
    n =  int(input())
    if n >= 0 and n < 21 :
        if n < pire_note:
            pire_note = n
        elif n > meilleure_note:
            meilleure_note = n 

        total += n   
    else:
        print("notes doit etre comprise en 0 et 20")

moyenne = total / nbre_eleve
print(f"Meilleure note : {meilleure_note}")
print(f"Pire note : {pire_note}")
print(f"Moyenne : {moyenne:.2f}")
