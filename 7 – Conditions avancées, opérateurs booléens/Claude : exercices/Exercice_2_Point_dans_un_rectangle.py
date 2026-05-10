# Exercice 2 — Intersection de rectangles

# Point
x = int(input())
y = int(input())

# Rectangle
xMin = int(input())
xMax = int(input())

yMin = int(input())
yMax = int(input())

if xMin < x < xMax and yMin < y < yMax:
    print("OUI")
else:
    print("NON")