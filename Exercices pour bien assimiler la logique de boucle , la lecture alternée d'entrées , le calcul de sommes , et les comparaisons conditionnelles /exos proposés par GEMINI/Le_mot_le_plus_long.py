phrase = input()

mots = phrase.split()
if mots:
    premier_mot = mots[0]
    for mot in mots[1:]:
        if len(mot) > len(premier_mot):
            premier_mot = mot
    print(premier_mot)
else:
    print("")