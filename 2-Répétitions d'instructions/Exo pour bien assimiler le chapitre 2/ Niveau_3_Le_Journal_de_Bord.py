total = 0

for i in range(16):
    case = i + 1
    if bouse():
        ramasser()
        total += 1
        print(f"Case {case} : Bouse trouvé {total}.")

    else:
        print(f"Case {case} Rien. {total}.")
    droite()
deposer()
print(total)