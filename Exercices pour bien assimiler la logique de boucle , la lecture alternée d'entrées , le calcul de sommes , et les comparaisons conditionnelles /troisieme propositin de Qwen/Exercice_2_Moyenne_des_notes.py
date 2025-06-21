nombre_de_notes = int(input())
total_notes = 0

for i in range(nombre_de_notes):
    chaque_note = int(input())
    total_notes += chaque_note
moyenne = total_notes / nombre_de_notes
print(moyenne)