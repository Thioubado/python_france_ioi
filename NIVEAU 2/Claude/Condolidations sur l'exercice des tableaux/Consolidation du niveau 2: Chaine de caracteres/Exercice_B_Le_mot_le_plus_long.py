# Exercice B — Le mot le plus long
phrase = input().split()

compte = 0
for mot in phrase:
    #mot = len(mot)
    if len(mot) > compte:
        compte = len(mot)
        record = mot
print(record)
