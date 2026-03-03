total = 0

for i in range(16):
    if bouse():
        ramasser()
        total += 1
    droite()
deposer()
print(total)