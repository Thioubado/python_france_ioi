#reference = 0
liste = int(input())
if liste == 0:
    print(0)
else:
    temp_1 = int(input())
    for _ in range(liste - 1):
        temperature = int(input())
        if abs(temperature) < abs(temp_1):
            temp_1 = temperature
        elif abs(temperature) == abs(temp_1):
            if temperature > 0:
                temp_1 = temperature
print(temp_1)