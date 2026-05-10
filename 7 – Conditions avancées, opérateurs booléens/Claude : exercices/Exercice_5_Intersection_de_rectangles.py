# Exercice 5 — Intersection de rectangles

x1Min = int(input())
x1Max = int(input())
y1Min = int(input())
y1Max = int(input())


x2Min = int(input())
x2Max = int(input())
y2Min = int(input())
y2Max = int(input())

x = (x1Min < x2Max) and (x2Min < x1Max)
y = (y1Min < y2Max) and (y2Min < y1Max)

if x and y :
    print("OUI")
else:
    print("NON")