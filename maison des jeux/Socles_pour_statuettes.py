grand_carre = int(input())
petit_carre = int(input())
volume = 0

for i in range(grand_carre, petit_carre - 1, -1):
    volume = volume + i * i
    """print(volume)"""
print(volume)