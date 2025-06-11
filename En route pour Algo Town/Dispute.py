point_Alga =  int(input())
point_Orthonart = int(input())
"""difference = abs(point_Alga - point_Orthonart)"""

if point_Orthonart > point_Alga + 10:
    print("Orthonart a trop de points.")
elif point_Alga > point_Orthonart + 10:
    print("Alga a trop de points.")


