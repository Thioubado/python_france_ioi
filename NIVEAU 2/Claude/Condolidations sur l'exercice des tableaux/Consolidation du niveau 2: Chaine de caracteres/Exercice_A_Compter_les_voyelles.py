# Exercice A — Compter les voyelles
phrase = input()

#print(phrase)  # a, e, i, o, u, y
result = 0
for lettre in phrase:
    if lettre == "a":
        result += 1
    elif lettre == "e":
        result += 1
    elif lettre == "i":
        result += 1
    elif lettre == "o":
        result += 1
    elif lettre == "u":
        result += 1
    elif lettre == "y":
        result += 1
print(result)