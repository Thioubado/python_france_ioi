point_de_départ  = int(input())

nombre_de_courses = int(input())

premiere_course = input()
valeurs = premiere_course.split()
nom_course = valeurs[0]
distance_course = int(valeurs[1])

for _ in range(nombre_de_courses - 1):
    autres_courses = input()
    valeur = autres_courses.split()
    course = valeur[0]
    distance = int(valeur[1])
    if distance < distance_course:
        distance_course = distance
        nom_course = course
print(nom_course, distance_course)