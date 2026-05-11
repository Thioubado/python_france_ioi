# La grande fête
date_de_début = int(input())
date_de_fin = int(input())

nbInvites = int(input())

invite_suspect = 0

for i in range(nbInvites):
    date_d_arrivee = int(input())
    date_de_depart = int(input())

    if date_d_arrivee <= date_de_fin and date_de_depart >= date_de_début:
        invite_suspect += 1
print(invite_suspect)