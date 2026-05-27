# Moyenne des notes
nombre_de_notes_obtenues = int(input())
result = 0
for _ in range(nombre_de_notes_obtenues):
    note = int(input())
    result += note

print(result / nombre_de_notes_obtenues)
